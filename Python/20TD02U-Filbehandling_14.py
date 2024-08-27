python
   # Skriv til flere filer
   for i in range(5):
       with open(f'file_{i}.txt', 'w') as file:
           file.write(f'This is file {i}')