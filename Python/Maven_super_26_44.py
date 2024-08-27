python
# Kopierer en binærfil
with open('original.bin', 'rb') as original, open('kopi.bin', 'wb') as kopi:
    kopi.write(original.read())