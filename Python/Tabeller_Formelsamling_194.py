python
def betinget_sannsynlighet(A_gitt_B, B):
  """
  Beregner den betingede sannsynligheten P(A|B).

  Args:
      A_gitt_B (float): Sannsynligheten for A gitt at B har inntruffet.
      B (float): Sannsynligheten for B.

  Returns:
      float: Den betingede sannsynligheten P(A|B).

  Raises:
      ValueError: Hvis A_gitt_B eller B er utenfor intervallet [0, 1].
  """
  if not (0 <= A_gitt_B <= 1) or not (0 <= B <= 1):
    raise ValueError("Sannsynligheter må være mellom 0 og 1.")
  return A_gitt_B * B

# Eksempelbruk:
A_gitt_B = 0.8  # Sannsynlighet for å bestå eksamen gitt at man har studert
B = 0.6  # Sannsynlighet for å studere
sannsynlighet_for_å_bestå = betinget_sannsynlighet(A_gitt_B, B)
print("Sannsynligheten for å bestå eksamen er:", sannsynlighet_for_å_bestå)  # Output: Sannsynligheten for å bestå eksamen er: 0.48