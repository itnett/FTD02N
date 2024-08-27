python
import os

hostname = "www.google.com"  # Eksempel på et eksternt nettsted (WAN)
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(hostname, "er oppe!")
else:
    print(hostname, "er nede!")