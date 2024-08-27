python
def desimal_til_binær(desimaltall):
  """Konverterer et desimaltall til binært."""
  if desimaltall == 0:
    return "0"
  binærtall = ""
  while desimaltall > 0:
    rest = desimaltall % 2
    binærtall = str(rest) + binærtall
    desimaltall //= 2
  return binærtall

def desimal_til_heksadesimal(desimaltall):
  """Konverterer et desimaltall til heksadesimalt."""
  if desimaltall == 0:
    return "0"
  heksadesimaltall = ""
  while desimaltall > 0:
    rest = desimaltall % 16
    heksadesimaltall = hex(rest)[2:].upper() + heksadesimaltall  # Bruker hex() og fjerner "0x"
    desimaltall //= 16
  return heksadesimaltall

# Eksempelbruk:
desimaltall = 255

binærtall = desimal_til_binær(desimaltall)
print(f"Desimaltall {desimaltall} er {binærtall} i binær form.")

heksadesimaltall = desimal_til_heksadesimal(desimaltall)
print(f"Desimaltall {desimaltall} er {heksadesimaltall} i heksadesimal form.")