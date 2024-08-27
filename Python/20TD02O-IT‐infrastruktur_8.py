python
  from scapy.all import *

  def packet_callback(packet):
      if packet.haslayer(IP):
          ip_src = packet[IP].src
          ip_dst = packet[IP].dst
          print(f"Packet: {ip_src} -> {ip_dst}")

  sniff(prn=packet_callback, store=0)