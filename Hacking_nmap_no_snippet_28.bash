#!/bin/bash

TARGET=$1
LOGFILE="scan_results.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

function log() {
    echo "[$TIMESTAMP] $1" | tee -a $LOGFILE
}

function scan() {
    log "Start scanning $TARGET"

    # Step 1: Ping scan to check if the target is up
    log "Step 1: Performing Ping scan to check if the target is up"
    nmap -sn $TARGET | tee -a $LOGFILE

    if [ $? -ne 0 ]; then
        log "Ping scan indicates the target is down. Exiting."
        exit 1
    fi

    # Step 2: SYN scan for open ports (least intrusive)
    log "Step 2: Performing SYN scan for open ports (least intrusive)"
    nmap -sS $TARGET -oN syn_scan.txt | tee -a $LOGFILE

    open_ports=$(grep ^[0-9] syn_scan.txt | cut -d '/' -f 1 | tr '\n' ',' | sed 's/,$//')
    if [ -z "$open_ports" ]; then
        log "No open ports found with SYN scan. Exiting."
        exit 1
    fi
    log "Open ports found: $open_ports"

    # Step 3: Version detection on open ports
    log "Step 3: Performing version detection on open ports"
    nmap -sV -p $open_ports $TARGET -oN version_detection.txt | tee -a $LOGFILE

    # Step 4: OS detection (slightly more intrusive)
    log "Step 4: Performing OS detection"
    nmap -O $TARGET -oN os_detection.txt | tee -a $LOGFILE

    # Step 5: TCP Connect scan on ports that did not respond to SYN scan (more intrusive)
    log "Step 5: Performing TCP Connect scan on ports that did not respond to SYN scan (more intrusive)"
    nmap -sT -p $open_ports $TARGET -oN tcp_connect_scan.txt | tee -a $LOGFILE

    # Step 6: UDP scan on common ports
    log "Step 6: Performing UDP scan on common ports"
    nmap -sU --top-ports 20 $TARGET -oN udp_scan.txt | tee -a $LOGFILE

    # Step 7: Perform FIN, Xmas, and Null scans (even more intrusive)
    log "Step 7: Performing FIN, Xmas, and Null scans"
    nmap -sF -p $open_ports $TARGET -oN fin_scan.txt | tee -a $LOGFILE
    nmap -sX -p $open_ports $TARGET -oN xmas_scan.txt | tee -a $LOGFILE
    nmap -sN -p $open_ports $TARGET -oN null_scan.txt | tee -a $LOGFILE

    # Step 8: Perform ACK scan to map out firewall rules
    log "Step 8: Performing ACK scan to map out firewall rules"
    nmap -sA -p $open_ports $TARGET -oN ack_scan.txt | tee -a $LOGFILE

    # Step 9: Idle scan to further probe stealthily
    log "Step 9: Performing Idle scan to further probe stealthily"
    nmap -sI <zombie_host> $TARGET -oN idle_scan.txt | tee -a $LOGFILE

    # Step 10: Use Hping for more granular control
    log "Step 10: Using Hping for more granular control"
    hping3 -S $TARGET -p $open_ports -c 1 | tee -a $LOGFILE
    hping3 -F $TARGET -p $open_ports -c 1 | tee -a $LOGFILE
    hping3 -UPF $TARGET -p $open_ports -c 1 | tee -a $LOGFILE

    # Step 11: Masscan for fast scanning of large networks
    log "Step 11: Using Masscan for fast scanning of large networks"
    masscan -p$open_ports $TARGET --rate=1000 | tee -a $LOGFILE

    # Step 12: Netcat for banner grabbing and deeper probing
    log "Step 12: Using Netcat for banner grabbing and deeper probing"
    for port in $(echo $open_ports | tr ',' ' '); do
        nc -vz $TARGET $port | tee -a $LOGFILE
    done

    log "Scanning completed for $TARGET"
}

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

scan