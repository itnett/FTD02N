sql
CREATE TABLE exponential_points (
    x INT,
    f_x DOUBLE
);

INSERT INTO exponential_points (x, f_x)
VALUES
(0, 2 * POW(3, 0)),
(1, 2 * POW(3, 1)),
(2, 2 * POW(3, 2)),
(3, 2 * POW(3, 3)),
(4, 2 * POW(3, 4));

SELECT * FROM exponential_points;