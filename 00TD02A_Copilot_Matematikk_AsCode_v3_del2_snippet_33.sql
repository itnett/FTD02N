-- Beregning av total energi i et lukket system
SELECT kinetic_energy, potential_energy, 
       kinetic_energy + potential_energy AS total_energy 
FROM EnergyConservation;