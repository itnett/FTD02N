sql
CREATE TABLE line_points (
    x INT,
    y INT
);

INSERT INTO line_points (x, y)
VALUES
(1, 2*1 + 3),
(2, 2*2 + 3),
(3, 2*3 + 3),
(4, 2*4 + 3),
(5, 2*5 + 3);

SELECT * FROM line_points;