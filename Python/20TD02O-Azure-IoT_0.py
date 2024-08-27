python
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "Your IoT Hub device connection string"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_telemetry():
    telemetry_data = {"temperature": 22.5, "humidity": 60}
    message = Message(str(telemetry_data))
    client.send_message(message)
    print("Message sent")

send_telemetry()