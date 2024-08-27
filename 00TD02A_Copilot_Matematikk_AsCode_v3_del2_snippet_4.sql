-- Example table for line points
CREATE TABLE LinePoints (
    line_id INT AUTO_INCREMENT PRIMARY KEY,
    point1_x DECIMAL(5, 2),
    point1_y DECIMAL(5, 2),
    point2_x DECIMAL(5, 2),
    point2_y DECIMAL(5, 2)
);

-- Insert sample data into LinePoints
INSERT INTO LinePoints (point1_x, point1_y, point2_x, point2_y) VALUES
(1, 2, 3, 4),
(2, 3, 4, 5);

-- Calculate slope and y-intercept for each line
SELECT point1_x, point1_y, point2_x, point2_y,
       (point2_y - point1_y) / (point2_x - point1_x) AS slope,
       point1_y - ((point2_y - point1_y) / (point2_x - point1_x)) * point1_x AS y_intercept
FROM LinePoints;