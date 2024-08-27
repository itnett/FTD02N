python
      import paho.mqtt.client as mqtt

      def on_connect(client, userdata, flags, rc):
          print(f"Connected with result code {rc}")

      client = mqtt.Client()
      client.tls_set(ca_certs="ca.crt", certfile="client.crt", keyfile="client.key")
      client.connect("mqtt.example.com", 8883, 60)
      client.loop_forever()