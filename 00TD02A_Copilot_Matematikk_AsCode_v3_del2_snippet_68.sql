SELECT mass, velocity, 
       0.5 * mass * POWER(velocity, 2) AS kinetic_energy 
FROM KineticEnergyCalculations;

SELECT mass, height, 
       mass * 9.81 * height AS potential_energy 
FROM PotentialEnergyCalculations;