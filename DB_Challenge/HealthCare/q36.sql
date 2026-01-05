-- 36. Get the number of patients in the following age groups:
-- o 10-20
-- o 20-30
-- o 30-40
-- o 40-50
-- o 50-60
-- o 60-70

SELECT 
    CASE 
        WHEN age BETWEEN 10 AND 20 THEN '10-20'
        WHEN age BETWEEN 21 AND 30 THEN '21-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        WHEN age BETWEEN 51 AND 60 THEN '51-60'
        WHEN age BETWEEN 61 AND 70 THEN '61-70'
    END AS age_group,
    COUNT(*) AS total_patients
FROM memberinfo
WHERE age BETWEEN 10 AND 70
GROUP BY age_group
ORDER BY age_group;