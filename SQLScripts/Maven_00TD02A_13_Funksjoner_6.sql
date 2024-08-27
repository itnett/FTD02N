sql
CREATE TABLE polynomial_points (
    x INT,
    P_x INT
);

INSERT INTO polynomial_points (x, P_x)
VALUES
(1, 1*1*1 - 6*1*1 + 11*1 - 6),
(2, 2*2*2 - 6*2*2 + 11*2 - 6),
(3, 3*3*3 - 6*3*3 + 11*3 - 6),
(4, 4*4*4 - 6*4*4 + 11*4 - 6),
(5, 5*5*5 - 6*5*5 + 11*5 - 6);

SELECT * FROM polynomial_points;