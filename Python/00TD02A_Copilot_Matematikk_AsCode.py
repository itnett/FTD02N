python
import math

# ... (Previous functions for sphere volume and quadratic equation)

# Briggske logaritmer (Signal loss calculation)
def signal_loss_db(power_out, power_in):
    return 10 * math.log10(power_out / power_in)

# Simulering av faseovergang (forenklet)
def phase_transition(substance, current_temp, target_temp):
    # Simulerte data (erstatt med reelle verdier)
    specific_heat = {"water": 4.18, "ice": 2.1} 
    latent_heat = {"water": 334} 

    energy_required = 0
    if substance == "water":
        if target_temp > 100: # Koking
            energy_required += (100 - current_temp) * specific_heat["water"]
            energy_required += latent_heat["water"]
        else:  
            energy_required += (target_temp - current_temp) * specific_heat["water"]

    return energy_required

# Test de nye funksjonene
print(signal_loss_db(10, 100))  # -10 dB loss
print(phase_transition("water", 25, 125)) # Energi nødvendig for å koke vann fra 25 grader