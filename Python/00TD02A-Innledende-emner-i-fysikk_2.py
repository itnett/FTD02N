python
# Demonstrating mass, weight, and density concepts in IT

# Server mass
server_mass_kg = 25  # Kilograms

# Gravitational acceleration (Earth)
g = 9.81  # m/s^2

# Server weight
server_weight_newtons = server_mass_kg * g

# Server dimensions (hypothetical)
server_width = 0.5  # meters
server_length = 1.0  # meters
server_height = 0.2  # meters

# Server volume
server_volume_cubic_meters = server_width * server_length * server_height

# Server density
server_density_kg_per_cubic_meter = server_mass_kg / server_volume_cubic_meters

# Output results
print(f"Server mass: {server_mass_kg} kg")
print(f"Server weight: {server_weight_newtons:.2f} N")
print(f"Server density: {server_density_kg_per_cubic_meter:.2f} kg/m³")