python
# Trinket-kode for Mål og Enheter

# Leksjon 5.1: Enheter og Forstavelser

def convert_units(value, from_unit, to_unit):
    units = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001
    }
    return value * units[from_unit] / units[to_unit]

# Eksempelbruk
print("Leksjon 5.1: Enheter og Forstavelser")
value = float(input("Skriv inn verdi: "))
from_unit = input("Fra enhet (km, m, cm, mm): ")
to_unit = input("Til enhet (km, m, cm, mm): ")
result = convert_units(value, from_unit, to_unit)
print(f"{value} {from_unit} er {result} {to_unit}")

# Leksjon 5.2: Omgjøring mellom Lengdeenheter

print("\nLeksjon 5.2: Omgjøring mellom Lengdeenheter")
value = float(input("Skriv inn lengde i meter: "))
to_unit = input("Til enhet (km, cm, mm): ")
result = convert_units(value, 'm', to_unit)
print(f"{value} meter er {result} {to_unit}")

# Leksjon 5.3: Omgjøring mellom Arealenheter

def convert_area(value, from_unit, to_unit):
    units = {
        'm2': 1,
        'cm2': 0.0001,
        'mm2': 0.000001
    }
    return value * units[from_unit] / units[to_unit]

print("\nLeksjon 5.3: Omgjøring mellom Arealenheter")
value = float(input("Skriv inn areal: "))
from_unit = input("Fra enhet (m2, cm2, mm2): ")
to_unit = input("Til enhet (m2, cm2, mm2): ")
result = convert_area(value, from_unit, to_unit)
print(f"{value} {from_unit} er {result} {to_unit}")

# Leksjon 5.4: Omkrets og Areal av Rektangler

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_rectangle_area(length, width):
    return length * width

print("\nLeksjon 5.4: Omkrets og Areal av Rektangler")
length = float(input("Skriv inn lengde: "))
width = float(input("Skriv inn bredde: "))
perimeter = calculate_rectangle_perimeter(length, width)
area = calculate_rectangle_area(length, width)
print(f"Omkrets: {perimeter} m, Areal: {area} m²")

# Leksjon 5.5: Areal av Parallellogram

def calculate_parallelogram_area(base, height):
    return base * height

print("\nLeksjon 5.5: Areal av Parallellogram")
base = float(input("Skriv inn grunnlinje: "))
height = float(input("Skriv inn høyde: "))
area = calculate_parallelogram_area(base, height)
print(f"Areal av parallellogram: {area} m²")

# Leksjon 5.6: Areal av Trekanter

def calculate_triangle_area(base, height):
    return 0.5 * base * height

print("\nLeksjon 5.6: Areal av Trekanter")
base = float(input("Skriv inn grunnlinje: "))
height = float(input("Skriv inn høyde: "))
area = calculate_triangle_area(base, height)
print(f"Areal av trekant: {area} m²")

# Leksjon 5.7: Tid

def convert_time(value, from_unit, to_unit):
    units = {
        'h': 3600,
        'min': 60,
        's': 1
    }
    return value * units[from_unit] / units[to_unit]

print("\nLeksjon 5.7: Tid")
value = float(input("Skriv inn tid: "))
from_unit = input("Fra enhet (h, min, s): ")
to_unit = input("Til enhet (h, min, s): ")
result = convert_time(value, from_unit, to_unit)
print(f"{value} {from_unit} er {result} {to_unit}")

# Leksjon 5.8: Å Regne med Tid

def add_time(time1, unit1, time2, unit2):
    total_seconds = convert_time(time1, unit1, 's') + convert_time(time2, unit2, 's')
    return total_seconds / 3600, (total_seconds % 3600) / 60

print("\nLeksjon 5.8: Å Regne med Tid")
time1 = float(input("Skriv inn første tidsverdi: "))
unit1 = input("Enhet for første tidsverdi (h, min, s): ")
time2 = float(input("Skriv inn andre tidsverdi: "))
unit2 = input("Enhet for andre tidsverdi (h, min, s): ")
hours, minutes = add_time(time1, unit1, time2, unit2)
print(f"Sum tid: {int(hours)} timer og {int(minutes)} minutter")

# Leksjon 5.9: Vei, Fart, Tid

def calculate_distance(speed, time):
    return speed * time

def calculate_speed(distance, time):
    return distance / time

def calculate_time(distance, speed):
    return distance / speed

print("\nLeksjon 5.9: Vei, Fart, Tid")
distance = float(input("Skriv inn avstand (km): "))
speed = float(input("Skriv inn fart (km/t): "))
time = calculate_time(distance, speed)
print(f"Tid: {time} timer")

# Leksjon 5.10: Omgjøring mellom Volumenheter

def convert_volume(value, from_unit, to_unit):
    units = {
        'm3': 1,
        'L': 0.001,
        'mL': 0.000001
    }
    return value * units[from_unit] / units[to_unit]

print("\nLeksjon 5.10: Omgjøring mellom Volumenheter")
value = float(input("Skriv inn volum: "))
from_unit = input("Fra enhet (m3, L, mL): ")
to_unit = input("Til enhet (m3, L, mL): ")
result = convert_volume(value, from_unit, to_unit)
print(f"{value} {from_unit} er {result} {to_unit}")

# Leksjon 5.11: Overflate og Volum av Rette Prismer

def calculate_prism_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

def calculate_prism_volume(length, width, height):
    return length * width * height

print("\nLeksjon 5.11: Overflate og Volum av Rette Prismer")
length = float(input("Skriv inn lengde: "))
width = float(input("Skriv inn bredde: "))
height = float(input("Skriv inn høyde: "))
surface_area = calculate_prism_surface_area(length, width, height)
volume = calculate_prism_volume(length, width, height)
print(f"Overflate: {surface_area} m², Volum: {volume} m³")

# Leksjon 5.12: Massetetthet

def calculate_density(mass, volume):
    return mass / volume

print("\nLeksjon 5.12: Massetetthet")
mass = float(input("Skriv inn masse (g): "))
volume = float(input("Skriv inn volum (cm3): "))
density = calculate_density(mass, volume)
print(f"Massetetthet: {density} g/cm³")

# Leksjon 5.13: Valuta

def convert_currency(amount, rate):
    return amount * rate

print("\nLeksjon 5.13: Valuta")
amount = float(input("Skriv inn beløp i opprinnelig valuta: "))
rate = float(input("Skriv inn vekslingskurs: "))
converted_amount = convert_currency(amount, rate)
print(f"{amount} i opprinnelig valuta er {converted_amount} i ny valuta")