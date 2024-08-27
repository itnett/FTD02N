sql
-- Beregning av sluttposisjon ved konstant fart
SELECT initial_position, velocity, time, 
       initial_position + velocity * time AS final_position 
FROM MotionAtConstantSpeed;