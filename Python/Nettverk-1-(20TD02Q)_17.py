python
import os

hostname = "www.google.com"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(f"{hostname} er oppe!")
else:
    print(f"{hostname} er nede!")