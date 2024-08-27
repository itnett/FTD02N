python
  import os

  def ping(host):
      response = os.system("ping -c 1 " + host)
      if response == 0:
          print(f"{host} is up!")
      else:
          print(f"{host} is down!")

  ping("192.168.1.1")