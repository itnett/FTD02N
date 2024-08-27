-- Example table for objects in motion
CREATE TABLE ObjectsInMotion (
    object_id INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(5, 2), -- in kilograms
    acceleration DECIMAL(5, 2) -- in meters per second squared
);

-- Insert sample data into ObjectsInMotion
INSERT INTO ObjectsInMotion (mass, acceleration) VALUES
(10, 9.81),
(5, 3.5);

-- Calculate force for each object
SELECT mass, acceleration, 
       mass * acceleration AS force 
FROM ObjectsInMotion;