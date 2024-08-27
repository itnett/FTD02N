CREATE TABLE LinearEquations (
    equation_id INT AUTO_INCREMENT PRIMARY KEY,
    a1 DECIMAL(5,2),
    b1 DECIMAL(5,2),
    c1 DECIMAL(5,2),
    a2 DECIMAL(5,2),
    b2 DECIMAL(5,2),
    c2 DECIMAL(5,2)
);

INSERT INTO LinearEquations (a1, b1, c1, a2, b2, c2) VALUES
(2, 3, 5, 4, -1, 3);

SELECT (c1*b2 - c2*b1) / (a1*b2 - a2*b1) AS x,
       (a1*c2 - a2*c1) / (a1*b2 - a2*b1) AS y
FROM LinearEquations;