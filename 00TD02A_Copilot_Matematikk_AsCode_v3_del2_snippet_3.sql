-- Example table for cube dimensions
CREATE TABLE Cubes (
    cube_id INT AUTO_INCREMENT PRIMARY KEY,
    length DECIMAL(5, 2) -- length of the side of the cube
);

-- Insert sample data into Cubes
INSERT INTO Cubes (length) VALUES
(3.0),
(4.5),
(2.1);

-- Calculate surface area and volume for each cube
SELECT length, 
       POWER(length, 3) AS volume, 
       6 * POWER(length, 2) AS surface_area 
FROM Cubes;