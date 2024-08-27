python
import logging
import socket
import subprocess
import os
from scapy.all import *
import ipaddress

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
    # (Her kan du bruke scapy til å sende pakker mellom enheter for å illustrere kommunikasjon)
    logger.info("Simulering av stjernetopologi")
    # ... (Implementer pakkesending/mottak for å vise kommunikasjon)

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

# ... (Legg til flere funksjoner for å dekke andre emner som nettverksprotokoller,
#     nettverkstjenester, trådløs teknologi, og simuleringsverktøy)

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter nettverkssimulering...")

    # LAN-oppsett
    configure_lan_interface("eth0", "192.168.1.10", "255.255.255.0")

    # Nettverkstopologier
    simulate_star_topology()

    # OSI-modellen
    demonstrate_mac_address_resolution()

    # IPv4 og IPv6
    display_ip_information()

    # ... (Kjør funksjoner for andre emner)

    logger.info("Nettverkssimulering fullført.")

if __name__ == "__main__":
    main()