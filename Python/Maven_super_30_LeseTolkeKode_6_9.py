python
import subprocess

def check_firewall_status():
    result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
    print("Firewall Status:\n", result.stdout)

def check_failed_logins():
    result = subprocess.run(['sudo', 'grep', 'Failed password', '/var/log/auth.log'], capture_output=True, text=True)
    print("Failed Login Attempts:\n", result.stdout)

def main():
    print("Running Security Audit...\n")
    
    check_firewall_status()
    check_failed_logins()

    print("Security Audit Completed.")

if __name__ == "__main__":
    main()