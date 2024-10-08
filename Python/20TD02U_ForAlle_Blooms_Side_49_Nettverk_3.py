python
import ipaddress

def calculate_subnets(ip, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
    return list(network.subnets())

subnets = calculate_subnets("192.168.1.0", 24)
for subnet in subnets:
    print(f"Subnet: {subnet}")