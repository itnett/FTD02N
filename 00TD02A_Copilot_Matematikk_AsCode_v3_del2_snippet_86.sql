CREATE TABLE Cubes (
    cube_id INT AUTO_INCREMENT PRIMARY KEY,
    length DECIMAL(5,2)
);

INSERT INTO Cubes (length) VALUES
(3.0),
(4.5),
(2.1);

SELECT length, 
       POWER(length, 3) AS volume, 
       6 * POWER(length, 2) AS surface_area 
FROM Cubes;