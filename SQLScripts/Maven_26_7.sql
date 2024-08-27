sql
  SELECT a.AccountName, b.BudgetAmount
  FROM Budget b
  JOIN Accounts a ON b.AccountID = a.AccountID
  WHERE b.Year = 2024;