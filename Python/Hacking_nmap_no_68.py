python
import subprocess
import time
import logging
from datetime import datetime

# Konfigurer logging
logging.basicConfig(filename='scan_results.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s')

def log(message):
    """Logger meldinger til konsollen og loggfilen."""
    print(message)
    logging.info(message)

def run_command(command):
    """Kjører en shell-kommando og logger utdata."""
    log(f"Kjører kommando: {' '.join(command)}")
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        log(result.stdout)
    except subprocess.CalledProcessError as e:
        log(f"Feil ved kjøring av kommando: {e}")
        log(e.output)

def parse_open_ports(filename):
    """Parser åpne porter fra en Nmap scan result-fil."""
    open_ports = []
    with open(filename, 'r') as file:
        for line in file:
            if '/open/' in line:
                open_ports.append(line.split('/')[0].strip())
    return open_ports

def scan(target):
    """Utfører en intelligent, multi-laget nettverksskanning på en gitt mål."""
    log(f"Starter skanning av {target}")

    # Step 1: ARP scan to check if the target is up (least disruptive)
    log("Step 1: Utfører ARP-skanning for å sjekke om målet er oppe")
    run_command(['nmap', '-sn', '-PR', target])

    # Step 2: DNS query to check for open services (very stealthy)
    log("Step 2: Utfører DNS-forespørsel for å sjekke åpne tjenester")
    run_command(['dig', target])

    # Step 3: Passive OS fingerprinting (completely passive)
    log("Step 3: Utfører passiv OS-fingeravtrykk")
    p0f_process = subprocess.Popen(['p0f', '-i', 'any', '-p'])
    time.sleep(60)
    p0f_process.terminate()

    # Step 4: SYN scan for open ports (still stealthy)
    log("Step 4: Utfører SYN-skanning for åpne porter")
    run_command(['nmap', '-sS', target, '-oN', 'syn_scan.txt'])

    open_ports = parse_open_ports('syn_scan.txt')
    if not open_ports:
        log("Ingen åpne porter funnet med SYN-skanning. Avslutter.")
        return

    open_ports_str = ','.join(open_ports)
    log(f"Åpne porter funnet: {open_ports_str}")

    # Step 5: Version detection on open ports
    log("Step 5: Utfører versjonsdeteksjon på åpne porter")
    run_command(['nmap', '-sV', '-p', open_ports_str, target, '-oN', 'version_detection.txt'])

    # Step 6: OS detection (slightly more intrusive)
    log("Step 6: Utfører OS-deteksjon")
    run_command(['nmap', '-O', target, '-oN', 'os_detection.txt'])

    # Step 7: TCP Connect scan on ports that did not respond to SYN scan (more intrusive)
    log("Step 7: Utfører TCP Connect-skanning på porter som ikke svarte på SYN-skanning")
    run_command(['nmap', '-sT', '-p', open_ports_str, target, '-oN', 'tcp_connect_scan.txt'])

    # Step 8: UDP scan on common ports
    log("Step 8: Utfører UDP-skanning på vanlige porter")
    run_command(['nmap', '-sU', '--top-ports', '20', target, '-oN', 'udp_scan.txt'])

    # Step 9: Perform FIN, Xmas, and Null scans (even more intrusive)
    log("Step 9: Utfører FIN, Xmas, og Null-skanninger")
    run_command(['nmap', '-sF', '-p', open_ports_str, target, '-oN', 'fin_scan.txt'])
    run_command(['nmap', '-sX', '-p', open_ports_str, target, '-oN', 'xmas_scan.txt'])
    run_command(['nmap', '-sN', '-p', open_ports_str, target, '-oN', 'null_scan.txt'])

    # Step 10: Perform ACK scan to map out firewall rules
    log("Step 10: Utfører ACK-skanning for å kartlegge brannmurregler")
    run_command(['nmap', '-sA', '-p', open_ports_str, target, '-oN', 'ack_scan.txt'])

    # Step 11: Idle scan to further probe stealthily
    log("Step 11: Utfører Idle-skanning for videre stealthy probing")
    run_command(['nmap', '-sI', '<zombie_host>', target, '-oN', 'idle_scan.txt'])

    # Step 12: Use Hping for more granular control
    log("Step 12: Bruker Hping for mer granular kontroll")
    run_command(['hping3', '-S', target, '-p', open_ports_str, '-c', '1'])
    run_command(['hping3', '-F', target, '-p', open_ports_str, '-c', '1'])
    run_command(['hping3', '-UPF', target, '-p', open_ports_str, '-c', '1'])

    # Step 13: Masscan for fast scanning of large networks
    log("Step 13: Bruker Masscan for rask skanning av store nettverk")
    run_command(['masscan', '-p' + open_ports_str, target, '--rate=1000'])

    # Step 14: Netcat for banner grabbing and deeper probing
    log("Step 14: Bruker Netcat for banner grabbing og dypere probing")
    for port in open_ports:
        run_command(['nc', '-vz', target, port])

    log(f"Skanning fullført for {target}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Bruk: python intelligent_scan.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]
    scan(target)