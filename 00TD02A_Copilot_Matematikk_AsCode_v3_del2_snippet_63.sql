SELECT measurement, 
       measurement * (1 + uncertainty) AS upper_bound, 
       measurement * (1 - uncertainty) AS lower_bound 
FROM MeasurementsWithUncertainty;