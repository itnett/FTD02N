python
# Beregning av resultatbudsjett for 2016
omsetning = 200000000  # Omsetning i kr
variable_kostnader = 0.6 * omsetning  # 60% av omsetningen
faste_kostnader = 50000000  # Faste kostnader i kr
driftsresultat = omsetning - variable_kostnader - faste_kostnader

driftsmargin = (driftsresultat / omsetning) * 100

print(f"Omsetning: {omsetning} kr")
print(f"Variable kostnader: {variable_kostnader} kr")
print(f"Faste kostnader: {faste_kostnader} kr")
print(f"Driftsresultat: {driftsresultat} kr")
print(f"Driftsmargin: {driftsmargin:.2f}%")