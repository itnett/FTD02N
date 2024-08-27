sql
CREATE TABLE Vectors (
    vector_id INT AUTO_INCREMENT PRIMARY KEY,
    x_component DECIMAL(5,2),
    y_component DECIMAL(5,2)
);

INSERT INTO Vectors (x_component, y_component) VALUES
(3.0, 4.0),
(5.0, 12.0);

SELECT vector_id, 
       SQRT(POWER(x_component, 2) + POWER(y_component, 2)) AS magnitude 
FROM Vectors;