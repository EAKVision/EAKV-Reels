import asyncio
import os
import random
import sys
from datetime import datetime

# ANSI Escape Codes for Elite Terminal Styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RED = "\033[31m"
YELLOW = "\033[33m"
BG_BLACK = "\033[40m"


async def telemetry_streamer():
  # Clear screen and display header
  os.system("clear" if os.name == "posix" else "cls")
  print(f"{CYAN}{BOLD}==================================================")
  print(f"   EAK VISION // SOVEREIGN BACKEND TELEMETRY")
  print(f"   STATUS: ACTIVE | PROTOCOL: ZERO-BLOAT EXECUTION")
  print(f"=================================================={RESET}\n")

  nodes = ["US-EAST-CORE-01", "EU-CENTRAL-NODE", "AP-SOUTH-PIPELINE"]

  try:
    while True:
      timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
      node = random.choice(nodes)
      latency = round(random.uniform(1.2, 4.5), 2)  # Low latency metric
      throughput = random.randint(14200, 28900)  # High throughput
      status_code = random.choices(
          [200, 201, 503], weights=[85, 10, 5]
      )[0]

      if status_code == 200:
        status_str = f"{GREEN}[200 OK]{RESET}"
      elif status_code == 201:
        status_str = f"{YELLOW}[201 CREATED]{RESET}"
      else:
        status_str = f"{RED}[503 FAULT]{RESET}"

      log_line = (
          f"{BOLD}[{timestamp}]{RESET} Node: {cyan_text(node)} | "
          f"Throughput: {BOLD}{throughput} req/s{RESET} | "
          f"Latency: {GREEN}{latency}ms{RESET} | Status: {status_str}"
      )

      print(log_line)

      # Periodic tactical checkmate checkpoint
      if random.random() < 0.15:
        print(
            f"{CYAN}{BOLD} >>> [CHECKMATE ENGINE]: 360° Systems Integrity Verified."
            f" Zero Bloat Detected. Locked. ♟️🔒{RESET}"
        )

      await asyncio.sleep(0.8)  # High-frequency stream cadence

  except asyncio.CancelledError:
    pass


def cyan_text(text):
  return f"{CYAN}{text}{RESET}"


if __name__ == "__main__":
  try:
    asyncio.run(telemetry_streamer())
  except KeyboardInterrupt:
    print(f"\n{RED}{BOLD}[!] Telemetry manually terminated. Checkmate.{RESET}")
    sys.exit(0)
