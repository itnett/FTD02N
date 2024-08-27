sql
CREATE TABLE derivative_points (
    x INT,
    P_x INT,
    dP_dx INT
);

INSERT INTO derivative_points (x, P_x, dP_dx)
VALUES
(1, 1*1*1 - 6*1*1 + 11*1 - 6, 3*1*1 - 12*1 + 11),
(2, 2*2*2 - 6*2*2 + 11*2 - 6, 3*2*2 - 12*2 + 11),
(3, 3*3*3 - 6*3*3 + 11*3 - 6, 3*3*3 - 12*3 + 11),
(4, 4*4*4 - 6*4*4 + 11*4 - 6, 3*4*4 - 12*4 + 11),
(5, 5*5*5 - 6*5*5 + 11*5 - 6, 3*5*5 - 12*5 + 11);

SELECT * FROM derivative_points;