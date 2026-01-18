-- 42. Get the list of males who have blood pressure > 140 and have not had a heart attack.

SELECT DISTINCT m.*, b.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.gender = '0'
  AND b.bloodpressure > 140
  AND c.cardioarrestdetected=0;