python
from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Kilde-IP: {ip_layer.src}, Destinasjon-IP: {ip_layer.dst}")

sniff(iface="eth0", prn=packet_callback, count=5)  # Sniffer 5 pakker på grensesnittet "eth0"