-- 43. Get the list of members who had a heart attack from the state "Mountain Province".

SELECT DISTINCT m.*,a.state
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE  c.cardioarrestdetected=1
  AND a.state = 'Mountain Province';