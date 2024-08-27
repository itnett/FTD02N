python
@app.template_filter('formater_ip_adresse')
def formater_ip_adresse(ip_adresse):
    return ipaddress.ip_address(ip_adresse).exploded

# Bruk i mal:
<p>IP-adresse: {{ ip_adresse | formater_ip_adresse }}</p>