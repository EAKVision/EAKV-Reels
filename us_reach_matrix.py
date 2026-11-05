import datetime

US_TECH_HASHTAGS = [
    "#cprogramming", "#systemssoftware", "#computerarchitecture",
    "#softwareengineering", "#linuxkernel", "#baremetal",
    "#faang", "#backenddeveloper", "#codinglife", "#techmotivation"
]

def get_us_posting_schedule():
    # Target US Eastern Standard Time (EST)
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_est = now_utc.astimezone(datetime.timezone(datetime.timedelta(hours=-5)))
    
    print(f"[*] Current UTC Time : {now_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"[*] Current US EST   : {now_est.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    
    hour = now_est.hour
    if 8 <= hour <= 13:
        status = "OPTIMAL: US Morning / Lunch Engagement Window Active"
    elif 17 <= hour <= 22:
        status = "OPTIMAL: US Evening / Prime Viewership Window Active"
    else:
        status = "OFF-PEAK: Scheduled posting recommended during US prime hours"
        
    return status

def generate_us_caption(title, c_file):
    hashtags = " ".join(US_TECH_HASHTAGS)
    caption = (
        f"{title}\n\n"
        f"Deep dive into bare-metal system architecture. Source codebase written in zero-warning C ({c_file}).\n\n"
        f"Comment 'CODE' below to receive direct link to repo.\n\n"
        f"Follow @amrkhedrrr for systems engineering & elite physical performance.\n\n"
        f"{hashtags}"
    )
    return caption

if __name__ == "__main__":
    print("=== AKV Elite System: US Reach Strategy Matrix ===")
    schedule_status = get_us_posting_schedule()
    print(f"[*] Schedule Check: {schedule_status}\n")
    
    sample_caption = generate_us_caption(
        title="WHY 99% CANNOT WRITE MALLOC IN C",
        c_file="my_malloc.c"
    )
    print("--- SAMPLE US OPTIMIZED CAPTION ---")
    print(sample_caption)
