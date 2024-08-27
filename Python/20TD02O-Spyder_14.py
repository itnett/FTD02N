python
  import paho.mqtt.client as mqtt

  def on_connect(client, userdata, flags, rc):
      print(f"Connected with result code {rc}")
      client.subscribe("test/topic")

  def on_message(client, userdata, msg):
      print(f"{msg.topic} {msg.payload}")

  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  client.connect("mqtt.eclipse.org", 1883, 60)
  client.loop_start()

  client.publish("test/topic", "Hello MQTT")

  time.sleep(10)
  client.loop_stop()