sql
-- Beregning av avstand mellom servere (forenklet eksempel)
-- Antar servere plassert i et 2D-plan
SELECT server1.server_name AS server1, 
       server2.server_name AS server2,
       SQRT(POW(server1.x_coordinate - server2.x_coordinate, 2) + 
            POW(server1.y_coordinate - server2.y_coordinate, 2)) AS distance
FROM ServerLocations server1
JOIN ServerLocations server2 ON server1.id < server2.id; -- Unngå duplikater og avstand til seg selv