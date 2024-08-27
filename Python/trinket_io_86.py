python
   # Totalt mekanisk energi bevart: KE_initial + PE_initial = KE_final + PE_final
   # Anta et objekt faller fra en høyde med initial potensiell energi og null initial kinetisk energi.
   initial_potential_energy = potential_energy
   initial_kinetic_energy = 0
   final_kinetic_energy = initial_potential_energy  # all potential energy is converted to kinetic energy
   final_potential_energy = 0

   total_initial_energy = initial_potential_energy + initial_kinetic_energy
   total_final_energy = final_kinetic_energy + final_potential_energy
   print(f"Total initial energi: {total_initial_energy} J")
   print(f"Total final energi: {total_final_energy} J")