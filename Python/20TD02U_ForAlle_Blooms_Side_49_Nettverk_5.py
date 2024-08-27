python
from scapy.all import *

def wifi_scan():
    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[

Dot11Elt].info.decode()
            bssid = pkt[Dot11].addr2
            print(f"SSID: {ssid}, BSSID: {bssid}")

    sniff(iface="wlan0", prn=packet_handler, count=10)

wifi_scan()