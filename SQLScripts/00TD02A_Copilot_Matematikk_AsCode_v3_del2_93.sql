sql
CREATE TABLE Materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(10,2),
    volume DECIMAL(10,2)
);

INSERT INTO Materials (mass, volume) VALUES
(1000, 2.5),
(1500, 3.0),
(2550, 4.0);

SELECT mass, volume, 
       mass / volume AS density 
FROM Materials;