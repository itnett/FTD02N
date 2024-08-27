-- Beregning av kraft ved hjelp av Newtons andre lov
SELECT mass, acceleration, 
       mass * acceleration AS force 
FROM ObjectsInMotion;