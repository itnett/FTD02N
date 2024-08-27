bash
#!/bin/bash

LOGFILE="/mnt/c/lab/mylab/logs/configure-ansible.log"

# Function to log messages
log_message() {
    local MESSAGE=$1
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $MESSAGE" | tee -a $LOGFILE
}

log_message "Starting Ansible configuration..."

# Update and upgrade the system
log_message "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y
if [ $? -ne 0 ]; then
    log_message "Failed to update and upgrade the system."
    exit 1
else
    log_message "System updated and upgraded successfully."
fi

# Install Ansible
log_message "Installing Ansible..."
sudo apt install ansible -y
if [ $? -ne 0 ]; then
    log_message "Failed to install Ansible."
    exit 1
else
    log_message "Ansible installed successfully."
fi

# Verify Ansible installation
ANSIBLE_VERSION=$(ansible --version)
log_message "Ansible version: $ANSIBLE_VERSION"