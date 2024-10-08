python
import logging
import socket
import subprocess
import os
from scapy.all import *

# Konfigurasjon
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- GRUNNLEGGENDE NETTVERKSOPPSETT ---
def configure_interface(interface, ip_address, subnet_mask):
    """Konfigurerer en nettverksgrensesnitt med en IP-adresse og subnettmaske."""
    try:
        subprocess.run(["sudo", "ifconfig", interface, ip_address, "netmask", subnet_mask, "up"], check=True)
        logger.info(f"Grensesnitt {interface} konfigurert med IP {ip_address}/{subnet_mask}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved konfigurasjon av grensesnitt: {e}")

def ping_host(host):
    """Pinger en vert for å sjekke tilgjengelighet."""
    try:
        output = subprocess.check_output(["ping", "-c", "4", host], universal_newlines=True)
        logger.info(f"Ping resultat:\n{output}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ping mislyktes: {e}")

# --- FEILSØKING AV NETTVERK ---
def traceroute_host(host):
    """Utfører traceroute for å finne ruten til en vert."""
    try:
        output = subprocess.check_output(["traceroute", host], universal_newlines=True)
        logger.info(f"Traceroute resultat:\n{output}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Traceroute mislyktes: {e}")

def capture_packets(interface, count=10):
    """Fanger nettverkspakker på en spesifisert grensesnitt."""
    try:
        packets = sniff(iface=interface, count=count)
        packets.show()
        wrpcap('captured_packets.pcap', packets)
        logger.info(f"Fanget {count} pakker på grensesnitt {interface}")
    except Exception as e:
        logger.error(f"Feil ved pakkeinnfanging: {e}")

# --- SIKKERHET I NETTVERK ---
def enable_firewall():
    """Aktiverer grunnleggende brannmurregler."""
    try:
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        subprocess.run(["sudo", "ufw", "default", "deny"], check=True)
        subprocess.run(["sudo", "ufw", "allow", "22"], check=True)  # Tillater SSH
        logger.info("Grunnleggende brannmur aktivert.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved aktivering av brannmur: {e}")

def disable_firewall():
    """Deaktiverer brannmuren."""
    try:
        subprocess.run(["sudo", "ufw", "disable"], check=True)
        logger.info("Brannmur deaktivert.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved deaktivering av brannmur: {e}")

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter nettverksoppsett og feilsøking...")

    # Nettverksoppsett
    configure_interface('eth0', '192.168.1.10', '255.255.255.0')
    
    # Sjekk tilkobling med ping
    ping_host('8.8.8.8')

    # Feilsøking
    traceroute_host('8.8.8.8')
    capture_packets('eth0')

    # Sikkerhet
    enable_firewall()
    # ... utfør andre sikkerhetstester ...
    disable_firewall()

    logger.info("Nettverksoppsett og feilsøking fullført.")

if __name__ == "__main__":
    main()