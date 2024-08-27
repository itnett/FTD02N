sql
CREATE TABLE Angles (
    angle_id INT AUTO_INCREMENT PRIMARY KEY,
    angle DECIMAL(5,2)
);

INSERT INTO Angles (angle) VALUES
(30),
(45),
(60);

SELECT angle, 
       SIN(RADIANS(angle)) AS sine, 
       COS(RADIANS(angle)) AS cosine, 
       TAN(RADIANS(angle)) AS tangent 
FROM Angles;