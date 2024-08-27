python
def gjeldende_siffer(tall):
  """
  Finner antall gjeldende siffer i et tall.

  Args:
      tall (float): Tallet som skal analyseres.

  Returns:
      int: Antall gjeldende siffer.
  """
  # Konverterer tallet til en streng og fjerner ledende nuller og desimalpunktum
  tall_str = str(tall).strip('0').replace('.', '')
  return len(tall_str)

# Eksempelbruk:
tall = 0.01230
siffer = gjeldende_siffer(tall)
print("Antall gjeldende siffer i", tall, "er:", siffer)  # Output: Antall gjeldende siffer i 0.0123 er: 4