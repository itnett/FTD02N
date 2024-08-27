sql
  SELECT d.DepartmentName, AVG(w.Rating) AS AvgRating
  FROM WorkEnvironment w
  JOIN Departments d ON w.DepartmentID = d.DepartmentID
  WHERE d.DepartmentName = 'HR'
  GROUP BY d.DepartmentName;