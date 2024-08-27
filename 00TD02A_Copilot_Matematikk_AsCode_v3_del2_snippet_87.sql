CREATE TABLE RightTriangles (
    triangle_id INT AUTO_INCREMENT PRIMARY KEY,
    a DECIMAL(5,2),
    b DECIMAL(5,2)
);

INSERT INTO RightTriangles (a, b) VALUES
(3.0, 4.0),
(5.0, 12.0);

SELECT a, b, 
       SQRT(POWER(a, 2) + POWER(b, 2)) AS hypotenuse 
FROM RightTriangles;