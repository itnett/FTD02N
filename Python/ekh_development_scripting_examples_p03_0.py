python
import re

log_file = "/var/log/auth.log"
pattern = r"Failed password for (invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"

def analyze_logs(log_file):
    with open(log_file, "r") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                user = match.group(2)
                ip_address = match.group(3)
                print(f"Suspicious activity detected: {user} from {ip_address}")

if __name__ == "__main__":
    analyze_logs(log_file)