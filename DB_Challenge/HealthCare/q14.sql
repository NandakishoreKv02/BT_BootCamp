-- 14. Get all symptom details for the month of July and year 2019

SELECT *
FROM symptom
WHERE EXTRACT(MONTH FROM date) = 7
  AND EXTRACT(YEAR FROM date) = 2019;