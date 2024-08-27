#!/bin/bash

TARGET=$1
LOGFILE="scan_results.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

function log() {
    echo "[$TIMESTAMP] $1" | tee -a $LOGFILE
}

function scan() {
    log "Start scanning $TARGET"

    # Step 1: ARP scan to check if the target is up (least disruptive)
    log "Step 1: Performing ARP scan to check if the target is up"
    nmap -sn -PR $TARGET | tee -a $LOGFILE

    if [ $? -ne 0 ]; then
        log "ARP scan indicates the target is down. Exiting."
        exit 1
    fi

    # Step 2: DNS query to check for open services (very stealthy)
    log "Step 2: Performing DNS query to check for open services"
    dig $TARGET | tee -a $LOGFILE

    # Step 3: Passive OS fingerprinting (completely passive)
    log "Step 3: Performing Passive OS fingerprinting"
    p0f -i any -p | tee -a $LOGFILE &
    P0F_PID=$!
    sleep 60
    kill $P0F_PID

    # Step 4: SYN scan for open ports (still stealthy)
    log "Step 4: Performing SYN scan for open ports"
    nmap -sS $TARGET -oN syn_scan.txt | tee -a $LOGFILE

    open_ports=$(grep ^[0-9] syn_scan.txt | cut -d '/' -f 1 | tr '\n' ',' | sed 's/,$//')
    if [ -z "$open_ports" ]; then
        log "No open ports found with SYN scan. Exiting."
        exit 1
    fi
    log "Open ports found: $open_ports"

    # Step 5: Version detection on open ports
    log "Step 5: Performing version detection on open ports"
    nmap -sV -p $open_ports $TARGET -oN version_detection.txt | tee -a $LOGFILE

    # Step 6: OS detection (slightly more intrusive)
    log "Step 6: Performing OS detection"
    nmap -O $TARGET -oN os_detection.txt | tee -a $LOGFILE

    # Step 7: TCP Connect scan on ports that did not respond to SYN scan (more intrusive)
    log "Step 7: Performing TCP Connect scan on ports that did not respond to SYN scan"
    nmap -sT -p $open_ports $TARGET -oN tcp_connect_scan.txt | tee -a $LOGFILE

    # Step 8: UDP scan on common ports
    log "Step 8: Performing UDP scan on common ports"
    nmap -sU --top-ports 20 $TARGET -oN udp_scan.txt | tee -a $LOGFILE

    # Step 9: Perform FIN, Xmas, and Null scans (even more intrusive)
    log "Step 9: Performing FIN, Xmas, and Null scans"
    nmap -sF -p $open_ports $TARGET -oN fin_scan.txt | tee -a $LOGFILE
    nmap -sX -p $open_ports $TARGET -oN xmas_scan.txt | tee -a $LOGFILE
    nmap -sN -p $open_ports $TARGET -oN null_scan.txt | tee -a $LOGFILE

    # Step 10: Perform ACK scan to map out firewall rules
    log "Step 10: Performing ACK scan to map out firewall rules"
    nmap -sA -p $open_ports $TARGET -oN ack_scan.txt | tee -a $LOGFILE

    # Step 11: Idle scan to further probe stealthily
    log "Step 11: Performing Idle scan to further probe stealthily"
    nmap -sI <zombie_host> $TARGET -oN idle_scan.txt | tee -a $LOGFILE

    # Step 12: Use Hping for more granular control
    log "Step 12: Using Hping for more granular control"
    hping3 -S $TARGET -p $open_ports -c 1 | tee -a $LOGFILE
    hping3 -F $TARGET -p $open_ports -c 1 | tee -a $LOGFILE
    hping3 -UPF $TARGET -p $open_ports -c 1 | tee -a $LOGFILE

    # Step 13: Masscan for fast scanning of large networks
    log "Step 13: Using Masscan for fast scanning of large networks"
    masscan -p$open_ports $TARGET --rate=1000 | tee -a $LOGFILE

    # Step 14: Netcat for banner grabbing and deeper probing
    log "Step 14: Using Netcat for banner grabbing and deeper probing"
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