bash
#!/bin/bash

# Sjekk brannmurstatus (UFW)
check_firewall_status() {
    sudo ufw status
}

# Sjekk mislykkede påloggingsforsøk
check_failed_logins() {
    sudo grep 'Failed password' /var/log/auth.log
}

# Sårbarhetsskanning med Lynis
vulnerability_scan() {
    sudo lynis audit system
}

# Hovedskript
main() {
    echo "Running Security Audit..."
    check_firewall_status
    check_failed_logins
    vulnerability_scan
    echo "Security Audit Completed."
}

main