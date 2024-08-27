python
import random

# Antall pakker som sendes og mottas
num_packets = 1000

# Generer tilfeldig data for pakker (0: normal, 1: mistenkelig)
packets = [random.choice([0, 0, 0, 1]) for _ in range(num_packets)]

# Analyser trafikken
normal_traffic = packets.count(0)
suspicious_traffic = packets.count(1)

# Sikkerhetsvurdering
suspicion_ratio = suspicious_traffic / num_packets * 100

print(f"Antall normale pakker: {normal_traffic}")
print(f"Antall mistenkelige pakker: {suspicious_traffic}")
print(f"Prosentandel mistenkelig trafikk: {suspicion_ratio:.2f}%")

# Advarsel hvis mistenkelig trafikk overstiger terskel
if suspicion_ratio > 5:
    print("Advarsel: Høy andel mistenkelig trafikk. Sikkerhetstiltak anbefales.")
else:
    print("Nettverkstrafikken ser normal ut.")