bash
# Sjekke Autodiscover-posten for domenet
nslookup -type=CNAME autodiscover.example.com

# Sjekke MX-poster for domenet
nslookup -type=MX example.com