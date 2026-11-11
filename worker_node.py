import asyncio
import json
import random
import socket
import sys
import psutil

COLLECTOR_IP = "127.0.0.1"
COLLECTOR_PORT = 9999

async def stream_telemetry(node_id: str, region: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[WORKER] {node_id} ({region}) beaming telemetry -> {COLLECTOR_IP}:{COLLECTOR_PORT}")
    while True:
        payload = {
            "node_id": node_id,
            "region": region,
            "cpu_pct": psutil.cpu_percent(interval=None),
            "mem_pct": psutil.virtual_memory().percent,
            "latency_ms": random.uniform(4.2, 28.5),
        }
        sock.sendto(json.dumps(payload).encode("utf-8"), (COLLECTOR_IP, COLLECTOR_PORT))
        await asyncio.sleep(1.0)

if __name__ == "__main__":
    n_id = sys.argv[1] if len(sys.argv) > 1 else "node-alpha-01"
    reg = sys.argv[2] if len(sys.argv) > 2 else "eu-west-1"
    asyncio.run(stream_telemetry(n_id, reg))
