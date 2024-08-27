bash
# Schedule a patch update for a host group
hammer job-invocation create \
  --job-template "Run Command - Ansible Default" \
  --inputs "command=yum update -y" \
  --hostgroup "RHEL-Servers"