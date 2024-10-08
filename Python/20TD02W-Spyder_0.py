python
import paramiko
import logging
import json
from scapy.all import *
import time

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- SSH-TILKOBLING OG KONFIGURASJON AV ROUTERE/SWITCHER ---
def ssh_connect(hostname, port, username, password):
    """Oppretter en SSH-tilkobling til en enhet."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    return client

def run_command(client, command):
    """Kjører en kommando på en enhet via SSH."""
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    logger.info(f"Kommando: {command}\nOutput: {output}")
    return output

# --- KONFIGURASJON AV VLAN OG ROUTING ---
def configure_vlan(client, vlan_id, vlan_name):
    """Konfigurerer et VLAN på en switch."""
    commands = [
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        "exit"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"VLAN {vlan_id} ({vlan_name}) konfigurert.")

def configure_routing(client, network, mask, gateway):
    """Konfigurerer routing på en router."""
    commands = [
        f"ip route {network} {mask} {gateway}"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"Routing for nettverk {network}/{mask} via gateway {gateway} konfigurert.")

# --- VPN KONFIGURASJON ---
def configure_vpn(client, vpn_name, local_ip, remote_ip):
    """Konfigurerer en VPN-tunnel."""
    commands = [
        f"crypto isakmp policy 1",
        "authentication pre-share",
        "encryption aes",
        "hash sha",
        "group 2",
        "lifetime 86400",
        "exit",
        f"crypto isakmp key {vpn_name} address {remote_ip}",
        f"crypto ipsec transform-set {vpn_name} esp-aes esp-sha-hmac",
        f"crypto map {vpn_name} 10 ipsec-isakmp",
        f"set peer {remote_ip}",
        f"set transform-set {vpn_name}",
        f"match address 101",
        "exit",
        f"interface Tunnel0",
        f"ip address {local_ip} 255.255.255.252",
        f"tunnel source GigabitEthernet0/0",
        f"tunnel destination {remote_ip}",
        f"crypto map {vpn_name}",
        "exit"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"VPN {vpn_name} konfigurert mellom {local_ip} og {remote_ip}.")

# --- PENETRASJONSTESTING MED SCAPY ---
def perform_port_scan(target_ip, port_range):
    """Utfører en enkel portscan."""
    logger.info(f"Starter portscan på {target_ip} i portområdet {port_range}")
    open_ports = []
    for port in port_range:
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
            open_ports.append(port)
            sr1(IP(dst=target_ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
    logger.info(f"Åpne porter på {target_ip}: {open_ports}")
    return open_ports

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_network_security_examples():
    logger.info("Starter eksempler på nettverkskonfigurasjon og sikkerhet...")

    # SSH-tilkobling til en enhet (bruk fiktive data for demonstrasjon)
    hostname = '192.168.1.1'
    port = 22
    username = 'admin'
    password = 'admin'
    client = ssh_connect(hostname, port, username, password)

    # Konfigurer VLAN
    configure_vlan(client, vlan_id=10, vlan_name='Test_VLAN')

    # Konfigurer routing
    configure_routing(client, network='192.168.10.0', mask='255.255.255.0', gateway='192.168.1.1')

    # Konfigurer VPN
    configure_vpn(client, vpn_name='Test_VPN', local_ip='192.168.1.2', remote_ip='203.0.113.1')

    # Utfør portscan
    perform_port_scan(target_ip='192.168.1.100', port_range=range(20, 1025))

    logger.info("Eksempler på nettverkskonfigurasjon og sikkerhet fullført.")

if __name__ == "__main__":
    run_network_security_examples()