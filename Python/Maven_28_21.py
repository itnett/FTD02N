python
    def firewall(ip_address, allowed_ips):
        if ip_address in allowed_ips:
            logging.info(f"Access granted for IP: {ip_address}")
            return True
        else:
            logging.warning(f"Access denied for IP: {ip_address}")
            return False

    allowed_ips = ['192.168.1.1', '192.168.1.2']
    firewall('192.168.1.3', allowed_ips)