bash
# Installere OWASP ZAP
sudo apt-get install zaproxy

# Kjøre OWASP ZAP for å skanne en nettapplikasjon
zap.sh -cmd -quickurl http://example.com -quickout report.html