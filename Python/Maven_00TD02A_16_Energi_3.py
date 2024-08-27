python
# Input: CPU-bruk i prosent, antall servere, driftstid i timer
cpu_usage = 75  # CPU-bruk i prosent
num_servers = 50  # Antall servere
power_per_server = 500  # Effekt per server i watt
hours_operated = 24  # Driftstid per dag i timer

# Beregn total effektforbruk
total_power = (power_per_server * (cpu_usage / 100)) * num_servers

# Beregn daglig energiforbruk i kWh
energy_consumption = (total_power * hours_operated) / 1000

# Print resultater
print(f"Total effektforbruk for {num_servers} servere ved {cpu_usage}% CPU-bruk: {total_power} watt")
print(f"Daglig energiforbruk: {energy_consumption} kWh")