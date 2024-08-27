python
   import numpy as np

   # Array of IP addresses
   ip_addresses = np.array([
       "192.168.1.1",
       "192.168.1.2",
       "192.168.1.3",
       "192.168.1.4",
   ])

   # Number of IP addresses
   num_addresses = ip_addresses.size
   print(f"Number of IP addresses: {num_addresses}")

   # Check if a specific IP address is in the array
   search_ip = "192.168.1.5"
   if search_ip in ip_addresses:
       print(f"{search_ip} is in the network.")
   else:
       print(f"{search_ip} is not in the network.")