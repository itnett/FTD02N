python
    def check_access(ip_address):
        allowed_ips = ['192.168.1.1', '192.168.1.2']
        if ip_address in allowed_ips:
            return "Access granted"
        else:
            return "Access denied"

    ip_to_check = '192.168.1.3'
    result = check_access(ip_to_check)
    print(result)