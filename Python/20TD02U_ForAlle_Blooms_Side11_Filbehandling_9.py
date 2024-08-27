python
import os

# Sjekke om en fil eksisterer
if os.path.exists('eksempel.txt'):
    print('Filen eksisterer.')

# Opprette en katalog
os.mkdir('ny_katalog')

# Slette en fil
os.remove('eksempel.txt')

# Flytte en fil
os.rename('gammel.txt', 'ny.txt')