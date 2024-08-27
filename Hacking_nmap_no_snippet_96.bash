#!/bin/bash

LOGFILE="scan_results.log"

log() {
    local message=$1
    echo "[$(date)] $message" | tee -a "$LOGFILE"
}

run_command() {
    local command="$*"
    log "Running command: $command"
    eval "$command" 2>&1 | tee -a "$LOGFILE"
}

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1
log "Starting scan of $target"

# Add scanning steps here
run_command "nmap -sP $target"

log "Scan completed for $target"