-- 9. Get all the members who are from cities 'Burgos' and 'Flora'.
SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city in ('Burgos', 'Flora');