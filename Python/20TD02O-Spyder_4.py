python
import logging
import socket
import subprocess
from azure.iot.device import IoTHubDeviceClient, Message
from scapy.all import *
import json
import time

# Konfigurasjon
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Azure IoT Hub Konfigurasjon ---
CONNECTION_STRING = "HostName=<Your-IoT-Hub-Name>.azure-devices.net;DeviceId=<Your-Device-Id>;SharedAccessKey=<Your-Device-Key>"
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

def create_iot_hub_client():
    """Oppretter en IoT Hub-klient."""
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        logger.info("Tilkoblet til Azure IoT Hub.")
        return client
    except Exception as e:
        logger.error(f"Feil ved tilkobling til IoT Hub: {e}")
        return None

def send_telemetry(client, temperature, humidity):
    """Sender telemetridata til IoT Hub."""
    msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
    message = Message(msg_txt_formatted)
    try:
        client.send_message(message)
        logger.info(f"Telemetridata sendt: {msg_txt_formatted}")
    except Exception as e:
        logger.error(f"Feil ved sending av telemetridata: {e}")

# --- Feilsøking av maskinvare ---
def check_device_connectivity(device_ip):
    """Sjekker enhets tilkobling via ping."""
    try:
        output = subprocess.check_output(["ping", "-c", "4", device_ip], universal_newlines=True)
        logger.info(f"Ping resultat for {device_ip}:\n{output}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ping mislyktes for {device_ip}: {e}")

def scan_network():
    """Skanner nettverket for tilkoblede enheter."""
    logger.info("Skanner nettverket for tilkoblede enheter...")
    result = subprocess.run(["sudo", "arp-scan", "-l"], capture_output=True, text=True)
    logger.info(f"Nettverksskanning resultat:\n{result.stdout}")

# --- Protokoller og standarder ---
def demonstrate_mqtt():
    """Demonstrerer sending av en melding over MQTT."""
    import paho.mqtt.client as mqtt

    broker = "test.mosquitto.org"
    port = 1883
    topic = "iot/test"
    message = "Hello IoT"

    def on_connect(client, userdata, flags, rc):
        logger.info(f"MQTT tilkoblet med kode {rc}")
        client.publish(topic, message)

    client = mqtt.Client()
    client.on_connect = on_connect

    try:
        client.connect(broker, port, 60)
        client.loop_start()
        time.sleep(1)
        client.loop_stop()
        logger.info(f"MQTT melding sendt til {topic}: {message}")
    except Exception as e:
        logger.error(f"Feil ved MQTT-tilkobling: {e}")

# --- Simulering av sensordata ---
def simulate_sensor_data():
    """Simulerer innsamling og sending av sensordata til IoT Hub."""
    client = create_iot_hub_client()
    if client:
        try:
            while True:
                temperature = round(random.uniform(20.0, 25.0), 2)
                humidity = round(random.uniform(30.0, 50.0), 2)
                send_telemetry(client, temperature, humidity)
                time.sleep(10)
        except KeyboardInterrupt:
            logger.info("Simulering av sensordata avbrutt.")
        finally:
            client.disconnect()

# --- Sikkerhet i IoT ---
def enable_firewall():
    """Aktiverer grunnleggende brannmurregler."""
    try:
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        subprocess.run(["sudo", "ufw", "default", "deny"], check=True)
        subprocess.run(["sudo", "ufw", "allow", "22"], check=True)  # Tillater SSH
        logger.info("Grunnleggende brannmur aktivert.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved aktivering av brannmur: {e}")

def disable_firewall():
    """Deaktiverer brannmuren."""
    try:
        subprocess.run(["sudo", "ufw", "disable"], check=True)
        logger.info("Brannmur deaktivert.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved deaktivering av brannmur: {e}")

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter IoT og maskinvare simulering...")

    # Azure IoT Hub
    simulate_sensor_data()

    # Maskinvare feilsøking
    check_device_connectivity("192.168.1.1")
    scan_network()

    # Protokoller og standarder
    demonstrate_mqtt()

    # Sikkerhet
    enable_firewall()
    time.sleep(10)
    disable_firewall()

    logger.info("IoT og maskinvare simulering fullført.")

if __name__ == "__main__":
    main()