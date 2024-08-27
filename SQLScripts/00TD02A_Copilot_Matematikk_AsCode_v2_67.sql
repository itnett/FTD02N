sql
-- Beregning av linjens stigningstall og skjæringspunkt
SELECT point1_x, point1_y, point2_x, point2_y,
       (point2_y - point1_y) / (point2_x - point1_x) AS slope,
       point1_y - ((point2_y - point1_y) / (point2_x - point1_x)) * point1_x AS y_intercept
FROM LinePoints;