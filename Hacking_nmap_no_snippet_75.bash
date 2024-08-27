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

parse_open_ports() {
    local filename=$1
    grep '/open/' "$filename" | awk -F '/' '{print $1}' | tr '\n' ',' | sed 's/,$//'
}

scan() {
    local target=$1
    log "Starter skanning av $target"

    # Step 1: ARP scan to check if the target is up (least disruptive)
    log "Step 1: Utfører ARP-skanning for å sjekke om målet er oppe"
    run_command "nmap -sn -PR $target"

    # Step 2: DNS query to check for open services (very stealthy)
    log "Step 2: Utfører DNS-forespørsel for å sjekke åpne tjenester"
    run_command "dig $target"

    # Step 3: Passive OS fingerprinting (completely passive)
    log "Step 3: Utfører passiv OS-fingeravtrykk"
    p0f -i any -p &
    p0f_pid=$!
    sleep 60
    kill "$p0f_pid"

    # Step 4: SYN scan for open ports (still stealthy)
    log "Step 4: Utfører SYN-skanning for åpne porter"
    run_command "nmap -sS $target -oN syn_scan.txt"

    open_ports=$(parse_open_ports syn_scan.txt)
    if [ -z "$open_ports" ]; then
        log "Ingen åpne porter funnet med SYN-skanning. Avslutter."
        exit 1
    fi
    log "Åpne porter funnet: $open_ports"

    # Step 5: Version detection on open ports
    log "Step 5: Utfører versjonsdeteksjon på åpne porter"
    run_command "nmap -sV -p $open_ports $target -oN version_detection.txt"

    # Step 6: OS detection (slightly more intrusive)
    log "Step 6: Utfører OS-deteksjon"
    run_command "nmap -O $target -oN os_detection.txt"

    # Step 7: TCP Connect scan on ports that did not respond to SYN scan (more intrusive)
    log "Step 7: Utfører TCP Connect-skanning på porter som ikke svarte på SYN-skanning"
    run_command "nmap -sT -p $open_ports $target -oN tcp_connect_scan.txt"

    # Step 8: UDP scan on common ports
    log "Step 8: Utfører UDP-skanning på vanlige porter"
    run_command "nmap -sU --top-ports 20 $target -oN udp_scan.txt"

    # Step 9: Perform FIN, Xmas, and Null scans (even more intrusive)
    log "Step 9: Utfører FIN, Xmas, og Null-skanninger"
    run_command "nmap -sF -p $open_ports $target -oN fin_scan.txt"
    run_command "nmap -sX -p $open_ports $target -oN xmas_scan.txt"
    run_command "nmap -sN -p $open_ports $target -oN null_scan.txt"

    # Step 10: Perform ACK scan to map out firewall rules
    log "Step 10: Utfører ACK-skanning for å kartlegge brannmurregler"
    run_command "nmap -sA -p $open_ports $target -oN ack_scan.txt"

    # Step 11: Idle scan to further probe stealthily
    log "Step 11: Utfører Idle-skanning for videre stealthy probing"
    run_command "nmap -sI <zombie_host> $target -oN idle_scan.txt"

    # Step 12: Use Hping for more granular control
    log "Step 12: Bruker Hping for mer granular kontroll"
    run_command "hping3 -S $target -p $open_ports -c 1"
    run_command "hping3 -F $target -p $open_ports -c 1"
    run_command "hping3 -UPF $target -p $open_ports -c 1"

    # Step 13: Masscan for fast scanning of large networks
    log "Step 13: Bruker Masscan for rask skanning av store nettverk"
    run_command "masscan -p $open_ports $target --rate=1000"

    # Step 14: Netcat for banner grabbing and deeper probing
    log "Step 14: Bruker Netcat for banner grabbing og dypere probing"
    for port in ${open_ports//,/ }
    do
        run_command "nc -vz $target $port"
    done

    log "Skanning fullført for $target"
}

if [ "$#" -ne 1 ]; then
    echo "Bruk: $0 <target>"
    exit 1
fi

target=$1
scan "$target"