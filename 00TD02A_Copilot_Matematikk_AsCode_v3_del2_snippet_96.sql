CREATE TABLE WorkCalculations (
    work_id INT AUTO_INCREMENT PRIMARY KEY,
    force DECIMAL(10,2),
    distance DECIMAL(10,2)
);

INSERT INTO WorkCalculations (force, distance) VALUES
(100, 20),
(150, 15),
(200, 10);

SELECT force, distance, 
       force * distance AS work_done 
FROM WorkCalculations;