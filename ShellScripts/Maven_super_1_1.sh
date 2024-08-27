bash
# Eksempel på enkel serverovervåking med Bash
while true; do
  if ping -c 1 192.168.1.1 > /dev/null; then
    echo "Server is up"
  else
    echo "Server is down"
  fi
  sleep 60
done