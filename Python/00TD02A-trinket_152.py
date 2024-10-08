python
   # Energibevaring: Total mekanisk energi
   mass = 10  # kg
   initial_height = 20  # m
   initial_velocity = 0  # m/s
   gravitational_acceleration = 9.81  # m/s^2

   # Potensiell energi i starten
   initial_potential_energy = mass * gravitational_acceleration * initial_height
   # Kinetisk energi i starten
   initial_kinetic_energy = 0.5 * mass * initial_velocity**2
   total_initial_energy = initial_potential_energy + initial_kinetic_energy

   # Anta at objektet faller til bakken (høyde = 0 m)
   final_height = 0
   final_velocity = (2 * gravitational_acceleration * initial_height)**0.5  # Sluttfart ved bakken
   final_potential_energy = mass * gravitational_acceleration * final_height
   final_kinetic_energy = 0.5 * mass * final_velocity**2
   total_final_energy = final_potential_energy + final_kinetic_energy

   print(f"Total initial energi: {total_initial_energy} J")
   print(f"Total slutt energi: {total_final_energy} J")