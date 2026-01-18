-- 45. Get the count of members from "Mountain Province" aged between 50 and 60.

SELECT COUNT(*) AS total_members
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
  AND m.age BETWEEN 50 AND 60;

