python
def til_standardform(tall):
  """Konverterer et tall til standardform.

  Args:
      tall (float): Tallet som skal konverteres.

  Returns:
      str: Tallet på standardform (f.eks., "3.14e+02").
  """
  return "{:.2e}".format(tall)  # Formaterer med to desimaler

def fra_standardform(tall_str):
  """Konverterer et tall fra standardform til vanlig desimaltall.

  Args:
      tall_str (str): Tallet på standardform (f.eks., "3.14e+02").

  Returns:
      float: Tallet som desimaltall.
  """
  return float(tall_str)

# Eksempelbruk:
tall = 314000
tall_str = "1.23e-05"

print(tall, "på standardform:", til_standardform(tall))  # Output: 314000 på standardform: 3.14e+05
print(tall_str, "som desimaltall:", fra_standardform(tall_str))  # Output: 1.23e-05 som desimaltall: 1.23e-05