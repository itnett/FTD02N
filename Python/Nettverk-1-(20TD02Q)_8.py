python
import ipaddress

def validate_ip(address):
    try:
        ip = ipaddress.ip_address(address)
        return f"{address} is a valid {ip.version} address."
    except ValueError:
        return f"{address} is not a valid IP address."

print(validate_ip("192.168.1.1"))
print(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(validate_ip("invalid_ip"))