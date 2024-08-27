python
   try:
       fil = open("data.txt", "r")
       data = fil.read()
   except FileNotFoundError:
       print("Filen ble ikke funnet!")
   finally:
       fil.close()