python
from pathlib import Path

# Nåværende arbeidskatalog
cwd = Path.cwd()
print(cwd)

# Liste filer i en katalog
for fil in cwd.iterdir():
    print(fil.name)

# Opprette en ny katalog
ny_katalog = cwd / 'ny_katalog'
ny_katalog.mkdir(exist_ok=True)

# Slette en katalog
ny_katalog.rmdir()