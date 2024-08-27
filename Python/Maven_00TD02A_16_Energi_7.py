python
import random

# Terskelverdi for temperatur
temperature_threshold = 70  # i grader Celsius

# Simulering av temperaturmålinger
def simulate_temperature_reading():
    return random.uniform(50, 85)

# Overvåkning
for _ in range(10):
    temperature = simulate_temperature_reading()
    print(f"Nåværende temperatur: {temperature:.2f} °C")
    
    if temperature > temperature_threshold:
        print("Advarsel: Temperatur overstiger sikker terskel! Sjekk kjølesystemet.")
    else:
        print("Temperaturen er innenfor trygge grenser.")
    print("-" * 50)