import asyncio
import json
import time
from collections import deque
from contextlib import asynccontextmanager
from typing import Dict, Set

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

UDP_HOST = "0.0.0.0"
UDP_PORT = 9999
NODE_TTL_SECONDS = 6.0

class TelemetryState:
    def __init__(self):
        self.nodes: Dict[str, dict] = {}
        self.clients: Set[WebSocket] = set()

    def ingest_heartbeat(self, payload: dict):
        node_id = payload.get("node_id", "unknown-node")
        now = time.time()
        if node_id not in self.nodes:
            self.nodes[node_id] = {
                "node_id": node_id,
                "region": payload.get("region", "local-wsl"),
                "latency_history": deque(maxlen=30),
                "packets_received": 0,
            }
        node = self.nodes[node_id]
        latency = round(payload.get("latency_ms", 0.0), 2)
        node["latency_ms"] = latency
        node["cpu_pct"] = round(payload.get("cpu_pct", 0.0), 1)
        node["mem_pct"] = round(payload.get("mem_pct", 0.0), 1)
        node["last_seen"] = now
        node["status"] = "ONLINE"
        node["packets_received"] += 1
        node["latency_history"].append(latency)

    def sweep_dead_nodes(self):
        now = time.time()
        for node_id, node in self.nodes.items():
            if now - node["last_seen"] > NODE_TTL_SECONDS:
                node["status"] = "OFFLINE"

    def snapshot(self) -> dict:
        self.sweep_dead_nodes()
        serialized_nodes = {}
        for k, v in self.nodes.items():
            serialized_nodes[k] = {
                **v,
                "latency_history": list(v["latency_history"]),
                "age_sec": round(time.time() - v["last_seen"], 1),
            }
        return {
            "timestamp": time.strftime("%H:%M:%S"),
            "active_count": sum(1 for n in self.nodes.values() if n["status"] == "ONLINE"),
            "total_nodes": len(self.nodes),
            "nodes": serialized_nodes,
        }

state = TelemetryState()

class TelemetryUDPProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr):
        try:
            payload = json.loads(data.decode("utf-8"))
            state.ingest_heartbeat(payload)
        except Exception:
            pass

async def broadcast_loop():
    while True:
        if state.clients:
            message = json.dumps(state.snapshot())
            dead_clients = set()
            for ws in state.clients:
                try:
                    await ws.send_text(message)
                except Exception:
                    dead_clients.add(ws)
            state.clients -= dead_clients
        await asyncio.sleep(0.5)

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        lambda: TelemetryUDPProtocol(),
        local_addr=(UDP_HOST, UDP_PORT),
    )
    broadcaster = asyncio.create_task(broadcast_loop())
    print(f"[CHECKMATE ENGINE] UDP Collector live on {UDP_HOST}:{UDP_PORT}")
    print(f"[CHECKMATE ENGINE] Live Dashboard ready at http://localhost:8000")
    yield
    broadcaster.cancel()
    transport.close()

app = FastAPI(lifespan=lifespan)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Checkmate Engine // Live Telemetry</title>
<style>
  body { background: #090b0e; color: #e2e8f0; font-family: 'Courier New', monospace; margin: 0; padding: 24px; }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 16px; margin-bottom: 24px; }
  .title { font-size: 20px; font-weight: bold; color: #38bdf8; letter-spacing: 1px; }
  .badge { background: #0f172a; border: 1px solid #334155; padding: 6px 12px; border-radius: 4px; font-size: 13px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }
  .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 16px; transition: border-color 0.2s; }
  .card.online { border-left: 4px solid #22c55e; }
  .card.offline { border-left: 4px solid #ef4444; opacity: 0.65; }
  .node-top { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 12px; }
  .status-on { color: #22c55e; }
  .status-off { color: #ef4444; }
  .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; font-size: 13px; background: #090b0e; padding: 10px; border-radius: 4px; }
  .metric-val { font-size: 16px; font-weight: bold; color: #f8fafc; margin-top: 4px; }
</style>
</head>
<body>
  <div class="header">
    <div class="title">♟️ CHECKMATE ENGINE // LIVE TELEMETRY</div>
    <div class="badge" id="summary">CONNECTING...</div>
  </div>
  <div class="grid" id="grid"></div>
  <script>
    const ws = new WebSocket(`ws://${location.host}/ws/telemetry`);
    const grid = document.getElementById("grid");
    const summary = document.getElementById("summary");
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      summary.textContent = `ACTIVE NODES: ${data.active_count}/${data.total_nodes} | UTC ${data.timestamp}`;
      grid.innerHTML = Object.values(data.nodes).map(n => `
        <div class="card ${n.status === 'ONLINE' ? 'online' : 'offline'}">
          <div class="node-top">
            <span>${n.node_id} [${n.region}]</span>
            <span class="${n.status === 'ONLINE' ? 'status-on' : 'status-off'}">${n.status}</span>
          </div>
          <div class="metrics">
            <div>LATENCY<div class="metric-val">${n.latency_ms} ms</div></div>
            <div>CPU<div class="metric-val">${n.cpu_pct}%</div></div>
            <div>MEM<div class="metric-val">${n.mem_pct}%</div></div>
          </div>
          <div style="font-size: 11px; color: #64748b; margin-top: 10px;">
            PKTS: ${n.packets_received} | LAST SEEN: ${n.age_sec}s ago
          </div>
        </div>
      `).join("");
    };
  </script>
</body>
</html>
"""

@app.get("/")
async def get_dashboard():
    return HTMLResponse(DASHBOARD_HTML)

@app.websocket("/ws/telemetry")
async def telemetry_ws(websocket: WebSocket):
    await websocket.accept()
    state.clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        state.clients.discard(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
