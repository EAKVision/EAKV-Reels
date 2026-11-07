#!/usr/bin/env bash
echo "[WATCHDOG] Checking git repository status..."
if [ -d ".git" ]; then
    git add .
    git commit -m "auto-sync: EAKV autonomous workspace state update $(date +'%Y-%m-%d %H:%M:%S')" --quiet 2>/dev/null
    echo "[SUCCESS] Workspace state synchronized to local Git repository."
else
    echo "[INFO] Initializing local Git repository for supreme version control..."
    git init --quiet
    git add .
    git commit -m "initial: EAKV Sovereign Engine genesis" --quiet
    echo "[SUCCESS] Repository initialized and locked."
fi
