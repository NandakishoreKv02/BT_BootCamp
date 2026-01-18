-- 17. Display all cardio diagnosis details where the first name starts with the letter "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%';