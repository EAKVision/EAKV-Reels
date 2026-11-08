#!/bin/bash
# ==================================================
#     EAKV-REELS MASTER COMMAND CENTER V6 (FINAL)
# ==================================================

while true; do
    clear
    echo "=================================================="
    echo "    EAKV-REELS MASTER COMMAND CENTER V6 (FINAL)"
    echo "=================================================="
    echo " 1. Run Organic Boost Protocol (active_target.json)"
    echo " 2. Run Autonomous Git Watchdog (Sync State)"
    echo " 3. Generate Code-to-Reel Visual Artifact"
    echo " 4. Execute Automated Social Publisher"
    echo " 5. Trigger Real-Time Event Dispatcher & Telemetry"
    echo " 6. Export Interview Proof-of-Work (Markdown)"
    echo " 7. Generate Interview Technical Talking-Point Brief"
    echo " 8. Sync GitHub README Telemetry"
    echo " 9. Track & Rotate Active Reel Matrix Performance"
    echo " 11. Run Women Reach & Aesthetic Optimization (python3 women_reach_optimizer.py)"
    echo " 10. Exit Hub"
    echo "=================================================="
    read -p "Select an option [1-11]: " choice

    case $choice in
        1)
            python3 boost_organic.py
            ;;
        2)
            ./git_watchdog.sh
            ;;
        3)
            python3 code_to_reel.py
            ;;
        4)
            python3 publisher.py
            ;;
        5)
            python3 event_dispatch.py
            ;;
        6)
            python3 proof_exporter.py
            ;;
        7)
            python3 interview_prep_gen.py
            ;;
        8)
            python3 update_readme.py
            ;;
        9)
            python3 track_reel_performance.py
            ;;
        11)
            python3 women_reach_optimizer.py
            ;;
        10)
            echo "Exiting Sovereign Hub V6. Total global execution achieved. ⚡"
            exit 0
            ;;
        *)
            echo "Invalid option. Please select between 1 and 11."
            ;;
    esac
    
    echo ""
    read -p "Press [Enter] to return to the Master Hub..."
done
