python
with open('ny_fil.bin', 'wb') as fil:
    fil.write(b'\xDE\xAD\xBE\xEF')  # Skriver binær data til filen