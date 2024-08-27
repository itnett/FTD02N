python
   # SI-prefikser for lengde
   meter = 1
   kilometer = 1e3 * meter
   centimeter = 1e-2 * meter
   millimeter = 1e-3 * meter

   # Eksempler på konvertering
   length_m = 10  # meter
   length_km = length_m / kilometer
   length_cm = length_m / centimeter
   length_mm = length_m / millimeter

   print(f"Lengde: {length_m} m = {length_km} km = {length_cm} cm = {length_mm} mm")