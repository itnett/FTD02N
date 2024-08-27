python
    # Simulere en temperatur sensor
    import random
    import time

    def simulate_temperature_sensor():
        while True:
            temperature = random.uniform(20.0, 30.0)  # Generere tilfeldig temperatur
            print(f"Temperatur: {temperature:.2f} C")
            time.sleep(5)  # Vent 5 sekunder før neste måling

    simulate_temperature_sensor()