python
import os
import shutil
import time

kildemappe = "/path/til/kildemappe"
destinasjonsmappe = "/path/til/destinasjonsmappe"
intervall = 3600  # Sekunder (1 time)

while True:
    shutil.copytree(kildemappe, destinasjonsmappe)
    print("Sikkerhetskopi fullført.")
    time.sleep(intervall)