sql
  SELECT t.TrainingName, t.TrainingDate
  FROM Trainings t
  JOIN Employees e ON t.EmployeeID = e.EmployeeID
  WHERE e.FirstName = 'John' AND e.LastName = 'Doe';