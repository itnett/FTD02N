CREATE TABLE ExponentialValues (
    exp_id INT AUTO_INCREMENT PRIMARY KEY,
    x DECIMAL(5,2)
);

INSERT INTO ExponentialValues (x) VALUES
(1),
(2),
(3);

SELECT x, 
       EXP(x) AS exp_value 
FROM ExponentialValues;