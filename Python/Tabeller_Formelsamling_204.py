python
def and_gate(a, b):
  """Simulerer en AND-port."""
  return a and b

def or_gate(a, b):
  """Simulerer en OR-port."""
  return a or b

def not_gate(a):
  """Simulerer en NOT-port."""
  return not a

# Eksempelbruk:
print("AND:", and_gate(True, False))  # Output: AND: False
print("OR:", or_gate(True, False))   # Output: OR: True
print("NOT:", not_gate(True))        # Output: NOT: False