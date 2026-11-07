import os
import json

class EAKVRepurposeEngine:
    def __init__(self, topic: str, c_code_snippet: str, athlete_context: str):
        self.topic = topic
        self.c_code_snippet = c_code_snippet
        self.athlete_context = athlete_context

    def generate_ig_tiktok_script(self) -> dict:
        return {
            "platform": "Instagram Reels & TikTok",
            "hook_text_overlay": f"Why low-level devs need {self.topic.lower()}.",
            "visual_direction": "0-2s: Split screen Neovim vs Barbell squat. 3-10s: Code debugging screen recording.",
            "voiceover": f"Most developers hide behind high-level frameworks. But when you manage memory manually while pushing your physical limits with {self.athlete_context}, you build real cognitive endurance.",
            "cta": "Comment 'SYSTEM' to get the full source code cheat sheet."
        }

    def generate_x_thread(self) -> list:
        return [
            f"1/ Manual memory management in C teaches you discipline that high-level languages obscure. Here is why {self.topic} matters:",
            f"2/ Code snippet:\n```c\n{self.c_code_snippet}\n```",
            f"3/ Just like training for {self.athlete_context}, if you don't clean up your allocation, system failure is inevitable.",
            "4/ Bookmark this for your next deep-work coding block."
        ]

    def generate_threads_post(self) -> str:
        return f"Be honest: How many low-level C developers here actively train hybrid ({self.athlete_context})? What does your weekly routine look like?"

    def generate_linkedin_carousel(self) -> dict:
        return {
            "platform": "LinkedIn PDF Carousel",
            "title": f"5 System Engineering Lessons from {self.topic}",
            "slides": [
                {"slide": 1, "title": "Zero-Cost Abstractions", "body": "Don't pay for performance you don't use."},
                {"slide": 2, "title": "Explicit Memory Management", "body": "Take 100% ownership of your resource lifecycle."},
                {"slide": 3, "title": "Deterministic Execution", "body": "Predictable daily habits beat volatile motivation every time."},
                {"slide": 4, "title": "Profiling & Bottleneck Auditing", "body": "Audit sleep and recovery before optimizing workload."},
                {"slide": 5, "title": "Compile-Time Verification", "body": "Catch failure points long before launch."}
            ]
        }

    def export_all(self, output_dir="output"):
        os.makedirs(output_dir, exist_ok=True)
        data = {
            "topic": self.topic,
            "ig_tiktok": self.generate_ig_tiktok_script(),
            "x_thread": self.generate_x_thread(),
            "threads": self.generate_threads_post(),
            "linkedin": self.generate_linkedin_carousel()
        }
        
        file_path = os.path.join(output_dir, f"{self.topic.lower().replace(' ', '_')}_package.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"[SUCCESS] Exported cross-platform content bundle to {file_path}")
        return data

if __name__ == "__main__":
    engine = EAKVRepurposeEngine(
        topic="Arena Allocators vs Malloc",
        c_code_snippet="typedef struct { char *buffer; size_t capacity; size_t offset; } Arena;",
        athlete_context="Zone-2 Running & 500lb Deadlifts"
    )
    engine.export_all()
