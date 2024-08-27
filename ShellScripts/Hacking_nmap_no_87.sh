bash
#!/bin/bash

LOGFILE="scan_results.log"

log() {
    local message=$1
    echo "[$(date)] $message" | tee -a "$LOGFILE"
}

run_command() {
    local command="$*"
    log "Kjører kommando: $command"
    eval "$command" 2>&1 | tee -a "$LOGFILE"
}

if [ "$#" -ne 1 ]; then
    echo "Bruk: $0 <target>"
    exit 1
fi

target=$1
log "Starter skanning av $target"

# Add scanning steps here

log "Skanning fullført for $target"