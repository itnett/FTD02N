python
def firewall_rule(packet):
    # Eksempelregel: Tillat hvis pakken kommer fra 192.168.0.0/16 og bruker port 80 eller 443
    ip_allowed = packet['src_ip'].startswith("192.168.")
    port_allowed = packet['port'] in [80, 443]
    is_allowed = ip_allowed and port_allowed
    
    return is_allowed

# Eksempel på pakke
packet = {'src_ip': '192.168.1.1', 'port': 80}
print("Packet allowed:", firewall_rule(packet))