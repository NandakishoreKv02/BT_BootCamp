-- 40. Get the list of females diagnosed with a heart attack.

SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '1'
  AND c.cardioarrestdetected=1;