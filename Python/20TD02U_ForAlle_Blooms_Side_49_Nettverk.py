python
def generate_acl(source_ip, dest_ip, action="permit"):
    acl_rule = f"access-list 101 {action} ip {source_ip} {dest_ip}"
    return acl_rule

print(generate_acl("192.168.1.0", "10.0.0.0", "deny"))