sql
  SELECT t.TransactionDate, t.Amount, t.Description
  FROM Transactions t
  JOIN Accounts a ON t.AccountID = a.AccountID
  WHERE a.AccountName = 'Driftskostnader';