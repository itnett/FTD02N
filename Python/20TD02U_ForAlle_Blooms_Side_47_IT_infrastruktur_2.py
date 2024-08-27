python
      import paho.mqtt.client as mqtt

      client = mqtt.Client()
      client.connect("mqtt.eclipse.org", 1883, 60)
      client.publish("sensor/temperature", "22.5")
      client.loop_forever()