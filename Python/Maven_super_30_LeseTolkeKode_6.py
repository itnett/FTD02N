python
import subprocess

def check_firewall_status():
    """
    Sjekker status på brannmur (UFW).
    """
    result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
    print("Firewall Status:\n", result.stdout)

def check_failed_logins():
    """
    Sjekker mislykkede påloggingsforsøk fra auth.log.
    """
    result = subprocess.run(['sudo', 'grep', 'Failed password', '/var/log/auth.log'], capture_output=True, text=True)
    print("Failed Login Attempts:\n", result.stdout)

def vulnerability_scan():
    """
    Kjør en sårbarhetsskanning med et verktøy som 'Lynis'.
    """
    try:
        result = subprocess.run(['sudo', 'lynis', 'audit', 'system'], capture_output=True, text=True)
        print("Vulnerability Scan Result:\n", result.stdout)
    except FileNotFoundError:
        print("Lynis is not installed. Please install it first.")

def main():
    print("Running Security Audit...\n")
    
    check_firewall_status()
    check_failed_logins()
    vulnerability_scan()

    print("Security Audit Completed.")

if __name__ == "__main__":
    main()