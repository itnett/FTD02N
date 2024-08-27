SELECT name, COUNT(*) as count
   FROM `mydataset.mytable`
   GROUP BY name
   ORDER BY count DESC;