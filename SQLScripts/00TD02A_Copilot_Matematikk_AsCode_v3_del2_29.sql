sql
-- Beregning av sluttposisjon ved konstant akselerasjon
SELECT initial_position, initial_velocity, acceleration, time, 
       initial_position + initial_velocity * time + 0.5 * acceleration * POWER(time, 2) AS final_position 
FROM MotionAtConstantAcceleration;