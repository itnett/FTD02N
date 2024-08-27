bash
#!/bin/bash

# Simulerer en IoT-enhet ved hjelp av funksjoner og arrays

declare -A IoTDevice

# Initialiserer en IoT-enhet
IoTDevice_Init() {
    IoTDevice[name]=$1
    IoTDevice[type]=$2
}

# Generer tilfeldig data
IoTDevice_GenerateData() {
    case ${IoTDevice[type]} in
        "Temperature Sensor") IoTDevice[data]=$(echo "scale=2; 20 + $RANDOM % 10" | bc) ;;
        "Humidity Sensor") IoTDevice[data]=$(echo "scale=2; 30 + $RANDOM % 40" | bc) ;;
        "Pressure Sensor") IoTDevice[data]=$(echo "scale=2; 950 + $RANDOM % 100" | bc) ;;
    esac
    IoTDevice[timestamp]=$(date --iso-8601=seconds)
}

# Send data til API (simulert)
IoTDevice_SendData() {
    local api_url=$1
    echo "Sending data to $api_url..."
    echo "Device: ${IoTDevice[name]}"
    echo "Type: ${IoTDevice[type]}"
    echo "Data: ${IoTDevice[data]}"
    echo "Timestamp: ${IoTDevice[timestamp]}"
}

# Hovedskript
main() {
    IoTDevice_Init "TempSensor1" "Temperature Sensor"
    IoTDevice_GenerateData
    IoTDevice_SendData "http://example.com/api/data"
}

main