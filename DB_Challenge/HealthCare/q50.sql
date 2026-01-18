-- 50. Get the average age of people diagnosed with a heart attack for each state, broken down by male
-- and female.

SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE c.cardioarrestdetected=1
GROUP BY a.state, m.gender
ORDER BY a.state, m.gender;
