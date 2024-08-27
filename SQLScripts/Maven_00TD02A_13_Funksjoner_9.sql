sql
CREATE TABLE regression_data (
    x INT,
    y INT
);

INSERT INTO regression_data (x, y)
VALUES
(1, 2),
(2, 3),
(3, 5),
(4, 6),
(5, 5);

SELECT * FROM regression_data;