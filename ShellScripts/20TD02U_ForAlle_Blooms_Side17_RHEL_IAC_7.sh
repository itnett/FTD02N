bash
# Krypter en fil med hemmeligheter
ansible-vault encrypt secrets.yml

# Bruk den krypterte filen i en playbook
---
- hosts: rhel_servers
  vars_files:
    - secrets.yml
  tasks:
    - name: Bruk en hemmelighet
      debug:
        msg: "Hemmelige data: {{ vault_secret_key }}"