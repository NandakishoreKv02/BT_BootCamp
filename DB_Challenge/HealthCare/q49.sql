-- 49. Get the count of people who have had their X-rays every month from the state of "Special
-- Province".

SELECT 
    EXTRACT(MONTH FROM x.date) AS month,
    COUNT(DISTINCT m.member_id) AS total_people
FROM xray x
JOIN cardiodiagnosis c 
    ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m 
    ON c.memberinfo_member_id = m.member_id
JOIN addressinfo a 
    ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Special Provinces'
GROUP BY EXTRACT(MONTH FROM x.date)
ORDER BY month;
