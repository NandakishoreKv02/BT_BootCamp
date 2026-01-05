-- 46. Get the count of male and female members who have blood pressure > 140 and have been
-- detected with a heart attack.

SELECT m.gender, COUNT(*) AS total_members
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140
  AND c.cardioarrestdetected=1
GROUP BY m.gender;