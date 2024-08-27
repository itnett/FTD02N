sql
CREATE TABLE KineticEnergyCalculations (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2),
    velocity DECIMAL(5, 2)
);

INSERT INTO KineticEnergyCalculations (mass, velocity) VALUES
(10, 15),
(5, 20);

SELECT mass, velocity, 
       0.5 * mass * POWER(velocity, 2) AS kinetic_energy 
FROM KineticEnergyCalculations;

CREATE TABLE PotentialEnergyCalculations (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2),
    height DECIMAL(5, 2)
);

INSERT INTO PotentialEnergyCalculations (mass, height) VALUES
(10, 10),
(5, 20);

SELECT mass, height, 
       mass * 9.81 * height AS potential_energy 
FROM PotentialEnergyCalculations;