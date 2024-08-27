# Eksempel på oppsett av en brannmurregel for å beskytte en databaseserver
sudo ufw allow from 192.168.1.0/24 to any port 3306 comment 'Tillat tilgang til MySQL fra lokalnettverket'

# Implementer en helhetlig løsning med kryptering, logging og tilgangskontroll