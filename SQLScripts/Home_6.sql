sql
SELECT CustomerID, SUM(Amount) 
FROM Orders 
WHERE OrderDate BETWEEN '2023-01-01' AND '2023-12-31' 
GROUP BY CustomerID;