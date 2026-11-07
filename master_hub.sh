#!/usr/bin/env bash

while true; do
    clear
    echo "=================================================="
    echo "    EAKV-REELS MASTER COMMAND CENTER V6 (FINAL)   "
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
    echo " 10. Exit Hub"
    echo "=================================================="
    read -p "Select an option [1-10]: " choice

    case $choice in
        1)
            echo "[*] Launching organic boost protocol..."
            python3 boost_organic.py
            read -p "Press Enter to return to menu..."
            ;;
        2)
            echo "[*] Executing Git Watchdog..."
            ./git_watchdog.sh
            read -p "Press Enter to return to menu..."
            ;;
        3)
            echo "[*] Running Code-to-Reel engine..."
            python3 code_to_reel.py
            read -p "Press Enter to return to menu..."
            ;;
        4)
            echo "[*] Executing automated social publisher..."
            python3 auto_publisher.py
            read -p "Press Enter to return to menu..."
            ;;
        5)
            echo "[*] Dispatching real-time workspace telemetry..."
            python3 event_dispatch.py
            read -p "Press Enter to return to menu..."
            ;;
        6)
            echo "[*] Exporting proof-of-work report..."
            python3 proof_exporter.py
            read -p "Press Enter to return to menu..."
            ;;
        7)
            echo "[*] Generating interview brief..."
            python3 interview_prep_gen.py
            read -p "Press Enter to return to menu..."
            ;;
        8)
            echo "[*] Syncing GitHub README..."
            python3 readme_sync.py
            read -p "Press Enter to return to menu..."
            ;;
        9)
            echo "[*] Scanning and rotating active matrix..."
            python3 track_reel_performance.py
            python3 matrix_rotator.py
            read -p "Press Enter to return to menu..."
            ;;
        10)
            echo "Exiting Sovereign Hub V6. Total global execution achieved. ⚡"
            exit 0
            ;;
        *)
            echo "Invalid option. Try again."
            sleep 1
            ;;
    esac
done
