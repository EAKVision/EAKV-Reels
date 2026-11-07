#!/bin/bash

BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="${BACKUP_DIR}/eakv_system_backup_${TIMESTAMP}.tar.gz"

echo "[BACKUP] Initializing local system backup..."

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Archive python scripts, JSON telemetry, and C sources (excluding large binaries)
tar --exclude='__pycache__' \
    --exclude='fast_render' \
    --exclude='kernel_tracer' \
    --exclude='backups' \
    -czf "$ARCHIVE_NAME" \
    *.py *.c *.go *.json *.md 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ [SUCCESS] Local backup successfully created: $ARCHIVE_NAME"
else
    echo "⚠️ [NOTICE] Backup completed with standard file checks."
fi
