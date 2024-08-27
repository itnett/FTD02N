sql
  SELECT InvestmentName, 
         InitialAmount * POWER(1 + (ExpectedReturn / 100), 5) AS FutureValue
  FROM Investments;