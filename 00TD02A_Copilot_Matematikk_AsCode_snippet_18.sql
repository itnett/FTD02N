-- Sannsynlighet for serverfeil basert på historiske data
SELECT server_name, 
       COUNT(CASE WHEN error_occurred = 1 THEN 1 END) / COUNT(*) AS failure_probability
FROM ServerLogs
GROUP BY server_name;