python
      import random
      import time
      from azure.iot.device import IoTHubDeviceClient, Message

      CONNECTION_STRING = "HostName=MyIoTHub.azure-devices.net;DeviceId=MyDevice;SharedAccessKey=YourKey"
      device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

      while True:
          temperature = random.uniform(20.0, 30.0)
          humidity = random.uniform(30.0, 70.0)
          msg = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')
          device_client.send_message(msg)
          time.sleep(10)