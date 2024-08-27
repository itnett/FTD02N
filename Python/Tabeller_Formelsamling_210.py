python
def prosent_til_desimaltall(prosent):
  """Konverterer en prosentverdi til desimaltall.

  Args:
      prosent (float): Prosentverdien.

  Returns:
      float: Desimaltallet som tilsvarer prosenten.
  """
  return prosent / 100

def desimaltall_til_prosent(desimaltall):
  """Konverterer et desimaltall til prosentverdi.

  Args:
      desimaltall (float): Desimaltallet.

  Returns:
      float: Prosentverdien som tilsvarer desimaltallet.
  """
  return desimaltall * 100

# Eksempelbruk:
prosent = 50
desimaltall = 0.75

print(prosent, "% =", prosent_til_desimaltall(prosent))  # Output: 50 % = 0.5
print(desimaltall, "=", desimaltall_til_prosent(desimaltall), "%")  # Output: 0.75 = 75.0 %