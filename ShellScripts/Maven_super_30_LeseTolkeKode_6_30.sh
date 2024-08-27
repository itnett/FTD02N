bash
#!/bin/bash

# Send data til et API med autentisering
send_data_to_api() {
    local api_url=$1
    local api_key=$2
    local data=$3

    curl -X POST "$api_url" \
         -H "Authorization: Bearer $api_key" \
         -H "Content-Type: application/json" \
         -d "$data"
}

# Hovedskript
main() {
    local api_url="https://your-iot-hub.azure-devices.net/devices/MyIoTDevice/messages/events?api-version=2018-06-30"
    local api_key="your_api_key_here"
    local data='{"temperature":22.5,"humidity":60}'

    send_data_to_api "$api_url" "$api_key" "$data"
}

main