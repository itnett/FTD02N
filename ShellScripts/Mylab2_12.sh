bash
#!/bin/bash

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y

# Install Ansible
sudo apt install ansible -y

# Verify Ansible installation
ansible --version