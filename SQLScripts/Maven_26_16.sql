sql
  SELECT s.SaleDate, s.Quantity, s.TotalPrice
  FROM Sales s
  JOIN Products p ON s.ProductID = p.ProductID
  WHERE p.ProductName = 'Sky Backup Service';