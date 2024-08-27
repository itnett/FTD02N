python
import re
from collections import Counter

# Function to parse log file
def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    log_data = []
    for line in logs:
        # Regex to extract timestamp, IP, and event type from log line
        match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), (\d+\.\d+\.\d+\.\d+), (.+)', line)
        if match:
            timestamp, ip_address, event_type = match.groups()
            log_data.append((timestamp, ip_address, event_type))
    return log_data

# Function to analyze log data
def analyze_logs(log_data):
    event_counter = Counter()
    ip_counter = Counter()

    for timestamp, ip_address, event_type in log_data:
        event_counter[event_type] += 1
        ip_counter[ip_address] += 1

    return event_counter, ip_counter

# Function to detect suspicious IP addresses
def detect_suspicious_ips(ip_counter, threshold=10):
    suspicious_ips = [ip for ip, count in ip_counter.items() if count > threshold]
    return suspicious_ips

# Example usage
if __name__ == "__main__":
    log_file_path = 'path_to_your_log_file.log'
    
    # Parse the log file
    logs = parse_log(log_file_path)
    
    # Analyze the logs
    event_counts, ip_counts = analyze_logs(logs)
    
    # Detect suspicious IP addresses
    suspicious_ips = detect_suspicious_ips(ip_counts)
    
    # Output results
    print("Event Counts:")
    for event, count in event_counts.items():
        print(f"{event}: {count}")
    
    print("\nSuspicious IP Addresses:")
    for ip in suspicious_ips:
        print(ip)