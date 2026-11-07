import os
from repurpose_engine import EAKVRepurposeEngine

topics = [
    {
        "topic": "Valgrind Memory Leak Detection",
        "code": "valgrind --leak-check=full ./main",
        "athlete": "Zone-2 Cardio & Track Sprints"
    },
    {
        "topic": "Stack vs Heap Allocation",
        "code": "int arr[100]; // Stack\nint *arr = malloc(100 * sizeof(int)); // Heap",
        "athlete": "Barbell Back Squats & Recovery Audits"
    },
    {
        "topic": "Pointer Arithmetic & Memory Boundaries",
        "code": "int *ptr = buffer;\nptr += 4; // Move by 4 elements",
        "athlete": "50-Mile Marathon Training Blocks"
    },
    {
        "topic": "GDB Line-by-Line Debugging",
        "code": "gdb ./program\n(gdb) break main\n(gdb) run",
        "athlete": "Zone-2 Running & 500lb Deadlifts"
    }
]

for t in topics:
    engine = EAKVRepurposeEngine(t["topic"], t["code"], t["athlete"])
    engine.export_all()

print("[SUCCESS] All Week 1 content packages generated in output/")
