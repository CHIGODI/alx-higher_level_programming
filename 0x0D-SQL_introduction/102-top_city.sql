-- diplay to 3 citiees with top temps in july , augst

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY CITY
ORDER BY avg_temp DESC
LIMIT 3;
