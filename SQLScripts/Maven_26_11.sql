sql
  SELECT e.FirstName, e.LastName, e.Position, e.Salary
  FROM Employees e
  JOIN Departments d ON e.DepartmentID = d.DepartmentID
  WHERE d.DepartmentName = 'IT';