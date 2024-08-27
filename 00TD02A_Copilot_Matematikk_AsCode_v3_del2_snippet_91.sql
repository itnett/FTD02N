CREATE TABLE PolynomialCoefficients (
    coeff_id INT AUTO_INCREMENT PRIMARY KEY,
    a DECIMAL(5,2),
    b DECIMAL(5,2),
    c DECIMAL(5,2),
    x DECIMAL(5,2)
);

INSERT INTO PolynomialCoefficients (a, b, c, x) VALUES
(1, 2, 3, 4),
(2, -1, 0, 3);

SELECT a, b, c, x,
       a*POWER(x, 2) + b*x + c AS polynomial_value 
FROM PolynomialCoefficients;