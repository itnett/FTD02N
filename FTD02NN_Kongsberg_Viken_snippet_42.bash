# IPTables eksempel
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Tillat SSH
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # Tillat HTTP
  sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT # Tillat HTTPS
  sudo iptables -A INPUT -j DROP                      # Drop all other traffic

  # OpenVPN server eksempel
  sudo apt-get install openvpn
  sudo openvpn --config /etc/openvpn/server.conf