-- 18. Display all cardio diagnosis details where the first name starts with "A" and ends with "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%a';