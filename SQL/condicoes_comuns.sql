SELECT condition_name, COUNT(*) AS total
FROM conditions
GROUP BY condition_name
ORDER BY total DESC
LIMIT 10;