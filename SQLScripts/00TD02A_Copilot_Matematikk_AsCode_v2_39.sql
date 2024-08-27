sql
-- Beregning av polynomverdi
SELECT x,
       a*POWER(x, 2) + b*x + c AS polynomial_value 
FROM PolynomialCoefficients;