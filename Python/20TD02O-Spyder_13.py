python
  from azure.iot.device import IoTHubDeviceClient, Message
  import random
  import time

  CONNECTION_STRING = "HostName=<Your-IoT-Hub-Name>.azure-devices.net;DeviceId=<Your-Device-Id>;SharedAccessKey=<Your-Device-Key>"
  MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

  def iothub_client_init():
      client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
      return client

  def send_telemetry(client):
      while True:
          temperature = round(random.uniform(20.0, 25.0), 2)
          humidity = round(random.uniform(30.0, 50.0), 2)
          msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
          message = Message(msg_txt_formatted)
          client.send_message(message)
          print(f"Sent message: {msg_txt_formatted}")
          time.sleep(10)

  if __name__ == "__main__":
      client = iothub_client_init()
      send_telemetry(client)