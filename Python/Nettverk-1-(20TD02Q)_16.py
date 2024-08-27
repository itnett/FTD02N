python
import pyshark

def capture_packets(interface):
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(packet_count=10)
    for packet in capture:
        print(packet)

capture_packets('eth0')