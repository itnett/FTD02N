bash
  #!/bin/bash
  while true
  do
    echo "CPU og minnebruk:"
    top -b -n 1 | grep "Cpu(s)" | awk '{print $2 + $4}' 
    free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
    sleep 5
  done