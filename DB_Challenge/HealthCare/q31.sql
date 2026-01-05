-- 31. Get the number of males and females aged between 50 and 60.
SELECT gender, COUNT(*) AS total_count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;