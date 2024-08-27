sql
-- Beregning av polynomverdi
SELECT 
    x, 
    a*POW(x, 2) + b*x + c AS polynomial_value 
FROM PolynomialCoefficients;