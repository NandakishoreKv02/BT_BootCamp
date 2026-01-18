-- 44. Get the list of male members and their diseases with symptoms for those aged less than 40.

SELECT m.*, d.*, s.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE m.gender = '0'
  AND m.age < 40;