import json

CALENDAR = [
    {"day": 1, "track": "Engineering", "module": "malloc_viral_1m.mp4", "hook": "Why 99% of Devs Can't Write Malloc in C", "pillar": "Bare-Metal C"},
    {"day": 2, "track": "Performance", "module": "fitness_discipline_01.mp4", "hook": "The Engineering Mindset Behind Peak Physical Training", "pillar": "Elite Fitness"},
    {"day": 3, "track": "Engineering", "module": "shell_viral_1m.mp4", "hook": "Building a Unix Shell from Scratch (fork + exec)", "pillar": "Systems Architecture"},
    {"day": 4, "track": "Engineering", "module": "io_bench_viral_1m.mp4", "hook": "POSIX write() vs High-Level I/O Benchmarking", "pillar": "Kernel Performance"},
    {"day": 5, "track": "Performance", "module": "recovery_protocol.mp4", "hook": "Sleep & Deep Work Optimization for Senior Engineers", "pillar": "Recovery & Focus"},
    {"day": 6, "track": "Engineering", "module": "vm_viral_1m.mp4", "hook": "Writing a Stack Bytecode Virtual Machine in C", "pillar": "Compilers & VMs"},
    {"day": 7, "track": "Engineering", "module": "tcp_viral_1m.mp4", "hook": "Raw Socket TCP Packet Sniffing at Kernel Level", "pillar": "Cybersecurity"},
    {"day": 8, "track": "Performance", "module": "training_routine.mp4", "hook": "Heavy Compound Lifts & Nervous System Recovery", "pillar": "Elite Fitness"},
]

def generate_calendar():
    print("=== AKV Elite System: 30-Day Content Calendar ===")
    for item in CALENDAR:
        print(f"[Day {item['day']:02d}] [{item['track'].upper()}] {item['hook']} -> Asset: {item['module']}")
    
    with open("30_day_calendar.json", "w") as f:
        json.dump(CALENDAR, f, indent=2)
    print("\n[✓] Saved 30_day_calendar.json for automated monthly scheduling.")

if __name__ == "__main__":
    generate_calendar()
