sql
CREATE TABLE Measurements (
    measurement_id INT AUTO_INCREMENT PRIMARY KEY,
    quantity_in_meters DECIMAL(10,2)
);

INSERT INTO Measurements (quantity_in_meters) VALUES
(1000),
(1500),
(2550);

SELECT quantity_in_meters, 
       quantity_in_meters / 1000 AS quantity_in_kilometers 
FROM Measurements;