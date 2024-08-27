SELECT vector_name, 
       SQRT(POWER(x_component, 2) + POWER(y_component, 2)) AS magnitude 
FROM Vectors;