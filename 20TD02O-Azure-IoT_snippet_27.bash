# Installere Snort på Ubuntu
sudo apt-get install snort

# Konfigurere Snort
sudo vi /etc/snort/snort.conf

# Starte Snort for å overvåke nettverkstrafikk
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0