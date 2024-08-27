-- Beregning av varmekapasitet
SELECT mass, specific_heat_capacity, temperature_change, 
       mass * specific_heat_capacity * temperature_change AS heat_energy 
FROM Calorimetry;