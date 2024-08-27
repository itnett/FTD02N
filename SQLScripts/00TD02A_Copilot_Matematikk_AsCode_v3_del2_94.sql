sql
CREATE TABLE MeasurementsWithUncertainty (
    measurement_id INT AUTO_INCREMENT PRIMARY KEY,
    measurement DECIMAL(10,2),
    uncertainty DECIMAL(5,2)
);

INSERT INTO MeasurementsWithUncertainty (measurement, uncertainty) VALUES
(100, 0.05),
(150, 0.10),
(250, 

0.20);

SELECT measurement, 
       measurement * (1 + uncertainty) AS upper_bound, 
       measurement * (1 - uncertainty) AS lower_bound 
FROM MeasurementsWithUncertainty;