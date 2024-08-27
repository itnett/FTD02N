python
import os
import logging
from datetime import datetime

# Setup logging
log_filename = 'server_log.txt'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_disk_space():
    # Simulate disk space check
    total, used, free = 100, 75, 25  # Example values in GB
    return total, used, free

def log_event(event):
    logging.info(event)

def main():
    print("Server Maintenance Log")
    
    # Check disk space
    total, used, free = check_disk_space()
    log_event(f"Disk space check: Total: {total}GB, Used: {used}GB, Free: {free}GB")
    
    # Simulate more server events
    log_event("System backup completed successfully.")
    log_event("Detected unauthorized access attempt.")
    
    # Read and display log file
    with open(log_filename, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()