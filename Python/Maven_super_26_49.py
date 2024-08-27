python
import os

# Nåværende arbeidskatalog
print(os.getcwd())

# Endre arbeidskatalog
os.chdir('/path/to/directory')

# Liste filer i en katalog
filer = os.listdir('.')
print(filer)