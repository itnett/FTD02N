python
import paramiko
import logging
import json
from scapy.all import *
import time
import socket
import re

# Sett opp logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- SSH-TILKOBLING OG KONFIGURASJON AV ROUTERE/SWITCHER ---
def ssh_connect(hostname, port, username, password):
    """Oppretter en SSH-tilkobling til en enhet med feilhåndtering."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        logger.info(f"SSH-tilkobling til {hostname} opprettet.")
        return client
    except (paramiko.AuthenticationException, paramiko.SSHException, socket.error) as e:
        logger.error(f"SSH-tilkobling mislyktes: {e}")
        return None

def run_command(client, command):
    """Kjører en kommando på en enhet via SSH med feilhåndtering."""
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        logger.info(f"Kommando: {command}\nOutput: {output}")
        return output
    except paramiko.SSHException as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")
        return None

# --- KONFIGURASJON AV VLAN, ROUTING, ACL ---
# ... (VLAN og routing funksjoner er de samme som før)

def configure_acl(client, acl_name, rule_number, action, protocol, source, destination):
    """Konfigurerer en ACL-regel på en router."""
    commands = [
        f"ip access-list extended {acl_name}",
        f"{rule_number} {action} {protocol} {source} {destination}",
        "exit"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"ACL-regel {rule_number} for {acl_name} konfigurert.")

# --- VPN KONFIGURASJON ---
# ... (VPN konfigurasjon funksjonen er den samme som før)

# --- PENETRASJONSTESTING MED SCAPY ---
# ... (Port scan funksjonen er den samme som før)

def perform_banner_grabbing(target_ip, port):
    """Utfører banner grabbing for å identifisere tjenester."""
    try:
        logger.info(f"Starter banner grabbing på {target_ip}:{port}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, port))
        banner = sock.recv(1024).decode()
        sock.close()
        logger.info(f"Banner på {target_ip}:{port}: {banner}")
        return banner
    except socket.error as e:
        logger.error(f"Banner grabbing mislyktes: {e}")
        return None

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_network_security_examples():
    logger.info("Starter eksempler på nettverkskonfigurasjon og sikkerhet...")

    # ... (SSH-tilkobling, VLAN, routing, VPN er de samme som før)

    # Konfigurer ACL
    configure_acl(client, acl_name='Test_ACL', rule_number=10, action='permit', protocol='tcp', source='any', destination='192.168.10.0 255.255.255.0 eq 80')

    # Utfør banner grabbing
    perform_banner_grabbing(target_ip='192.168.1.100', port=80)

    logger.info("Eksempler på nettverkskonfigurasjon og sikkerhet fullført.")

if __name__ == "__main__":
    run_network_security_examples()