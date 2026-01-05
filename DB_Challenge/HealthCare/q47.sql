-- 47. Get the average blood pressure of people aged between 40-50 and 50-60.

SELECT 
    CASE 
        WHEN m.age BETWEEN 40 AND 50 THEN '40-50'
        WHEN m.age BETWEEN 51 AND 60 THEN '51-60'
    END AS age_group,
    AVG(b.bloodpressure) AS avg_blood_pressure
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.age BETWEEN 40 AND 60
GROUP BY age_group
ORDER BY age_group;