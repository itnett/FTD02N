bash
# Bruk Ansible Tower CLI for å planlegge en jobb
tower-cli job launch --job-template="RHEL Patch Update" --schedule "0 2 * * *"