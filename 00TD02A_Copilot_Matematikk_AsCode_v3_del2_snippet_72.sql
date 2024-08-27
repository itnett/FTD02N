SELECT n, k, 
       FACT(n) / (FACT(k) * FACT(n - k)) AS combinations 
FROM Combinatorics;