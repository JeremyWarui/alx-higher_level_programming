-- Script that lists the number of records with the same score
-- Query to lists the number of records with the same score
--
-- score   number
-- 10  2
-- 8   1

SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC;
