python
  import psutil

  def monitor_network():
      net_io = psutil.net_io_counters()
      print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

  monitor_network()