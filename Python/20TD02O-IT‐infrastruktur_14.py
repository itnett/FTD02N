python
  import psutil

  def get_cpu_temp():
      temp = psutil.sensors_temperatures()
      return temp['coretemp'][0].current if 'coretemp' in temp else None

  cpu_temp = get_cpu_temp()
  print(f"CPU Temperatur: {cpu_temp}°C")