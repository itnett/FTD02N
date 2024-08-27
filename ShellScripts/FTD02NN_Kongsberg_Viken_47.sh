bash
  # Tillat SSH
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

  # Tillat HTTP og HTTPS
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

  # Dropp all annen trafikk
  sudo iptables -A INPUT -j DROP