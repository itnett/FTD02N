sql
  SELECT c.CampaignName, c.Budget, SUM(s.TotalPrice) - c.Budget AS ROI
  FROM MarketingCampaigns c
  JOIN Sales s ON s.SaleDate BETWEEN c.StartDate AND c.EndDate
  GROUP BY c.CampaignName, c.Budget;