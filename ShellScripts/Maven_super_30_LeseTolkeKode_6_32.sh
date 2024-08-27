bash
#!/bin/bash

# Overvåker ressursbruken til virtuelle maskiner
monitor_vms() {
    local cpu_usage=$(ps aux --sort=-%cpu | head -n 5)
    local mem_usage=$(ps aux --sort=-%mem | head -n 5)

    echo "CPU Usage:"
    echo "$cpu_usage"
    echo ""
    echo "Memory Usage:"
    echo "$mem_usage"
}

# Sende e-post alarm
send_alarm_email() {
    local vm_name=$1
    local cpu_usage=$2
    local mem_usage=$3

    echo "Warning! $vm_name is using $cpu_usage% CPU and $mem_usage% memory." | mail -s "High Resource Usage Alert for $vm_name" admin@yourcompany.com
}

# Hovedskript
main() {
    monitor_vms
    # Eksempel på alarm hvis CPU-bruken overstiger 80% (kan justeres)
    if [ $(ps aux --sort=-%cpu | awk 'NR==2 {print $3}') > 80 ]; then
        send_alarm_email "ExampleVM" 85 70
    fi
}

main