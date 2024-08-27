-- Example table for kinetic energy calculations
CREATE TABLE KineticEnergyCalculations (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2), -- in kilograms
    velocity DECIMAL(5, 2) -- in meters per second
);

-- Insert sample data into KineticEnergyCalculations
INSERT INTO KineticEnergyCalculations (mass, velocity) VALUES
(10, 15),
(5, 20);

-- Calculate kinetic energy for each object
SELECT mass, velocity, 
       0.5 * mass * POWER(velocity, 2) AS kinetic_energy 
FROM KineticEnergyCalculations;