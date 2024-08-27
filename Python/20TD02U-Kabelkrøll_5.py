python
import math

def beregn_kabelmengde(num_kveiler, d_inner, d_outer):
    # Beregn middelverdien av diameterne
    d_avg = (d_inner + d_outer) / 2  # cm
    # Beregn omkretsen til en sirkel med gjennomsnittlig diameter
    omkrets = math.pi * d_avg  # cm
    # Total lengde av kabelen
    total_length_cm = omkrets * num_kveiler  # cm
    total_length_m = total_length_cm / 100  # m
    return total_length_m

num_kveiler = 33
d_inner = 5  # cm
d_outer = 22  # cm

total_length_m = beregn_kabelmengde(num_kveiler, d_inner, d_outer)
print(f"Total lengde av kabelen på trommelen er ca. {total_length_m:.2f} meter.")