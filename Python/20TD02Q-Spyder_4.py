python
import logging
import socket
import subprocess
import os
from scapy.all import *

# Konfigurasjon
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- GRUNNLEGGENDE NETTVERKSOPPSETT (LAN) ---
def configure_lan_interface(interface, ip_address, subnet_mask):
    """Konfigurerer et LAN-grensesnitt med IP-adresse og subnettmaske."""
    try:
        subprocess.run(["sudo", "ip", "addr", "add", f"{ip_address}/{subnet_mask}", "dev", interface], check=True)
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"], check=True)
        logger.info(f"LAN-grensesnitt {interface} konfigurert med IP {ip_address}/{subnet_mask}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved konfigurasjon av LAN-grensesnitt: {e}")

# --- NETTVERKSTOPOLOGIER (Eksempel: Stjernetopologi) ---
def simulate_star_topology():
    """Simulerer en enkel stjernetopologi med en sentral switch og flere enheter."""
    logger.info("Simulering av stjernetopologi")
    # Eksempel: Sender ARP-pakker fra en sentral switch til flere enheter
    switch_ip = "192.168.1.1"
    for i in range(2, 6):
        target_ip = f"192.168.1.{i}"
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(psrc=switch_ip, pdst=target_ip)
        sendp(pkt, iface="eth0")
        logger.info(f"Sendt ARP-pakke til {target_ip}")

# --- OSI-MODELLEN (Eksempel: Lag 2 - Datakoblingslaget) ---
def demonstrate_mac_address_resolution():
    """Demonstrerer MAC-adresseoppløsning (ARP)."""
    try:
        my_mac = get_if_hwaddr(conf.iface)  # Får MAC-adressen til det lokale grensesnittet
        logger.info(f"Min MAC-adresse: {my_mac}")

        target_ip = "192.168.1.1"  # IP-adressen du vil løse opp
        target_mac = getmacbyip(target_ip)
        if target_mac:
            logger.info(f"MAC-adresse for {target_ip}: {target_mac}")
        else:
            logger.warning(f"Kunne ikke finne MAC-adresse for {target_ip}")
    except Exception as e:
        logger.error(f"Feil ved MAC-adresseoppløsning: {e}")

# --- IPv4 OG IPv6 ---
def display_ip_information():
    """Viser IPv4- og IPv6-informasjon for systemet."""
    try:
        ipv4 = socket.gethostbyname(socket.gethostname())
        ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
        logger.info(f"IPv4-adresse: {ipv4}")
        logger.info(f"IPv6-adresse: {ipv6}")
    except Exception as e:
        logger.error(f"Feil ved henting av IP-informasjon: {e}")

# --- NETTVERKSPROTOKOLLER ---
def demonstrate_tcp_connection(target_ip, target_port):
    """Demonstrerer opprettelsen av en TCP-tilkobling."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            logger.info(f"Opprettet TCP-tilkobling til {target_ip}:{target_port}")
            s.sendall(b"Hello, World!")
            data = s.recv(1024)
            logger.info(f"Mottatt data: {data}")
    except Exception as e:
        logger.error(f"Feil ved opprettelse av TCP-tilkobling: {e}")

# --- NETTVERKSTJENESTER (DNS-oppslag) ---
def perform_dns_lookup(domain):
    """Utfører DNS-oppslag for et gitt domenenavn."""
    try:
        ip_address = socket.gethostbyname(domain)
        logger.info(f"IP-adresse for {domain}: {ip_address}")
    except socket.error as e:
        logger.error(f"DNS-oppslag mislyktes for {domain}: {e}")

# --- TRÅDLØS TEKNOLOGI ---
def scan_wifi_networks():
    """Skanner tilgjengelige WiFi-nettverk (krever root-tilgang)."""
    try:
        networks = subprocess.check_output(["sudo", "iwlist", "scan"], universal_newlines=True)
        logger.info("Tilgjengelige WiFi-nettverk:\n" + networks)
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved skanning av WiFi-nettverk: {e}")

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter nettverkssimulering...")

    # LAN-oppsett
    configure_lan_interface("eth0", "192.168.1.10", "24")

    # Nettverkstopologier
    simulate_star_topology()

    # OSI-modellen
    demonstrate_mac_address_resolution()

    # IPv4 og IPv6
    display_ip_information()

    # Nettverksprotokoller
    demonstrate_tcp_connection("192.168.1.1", 80)

    # Nettverkstjenester
    perform_dns_lookup("example.com")

    # Trådløs teknologi
    scan_wifi_networks()

    logger.info("Nettverkssimulering fullført.")

if __name__ == "__main__":
    main()