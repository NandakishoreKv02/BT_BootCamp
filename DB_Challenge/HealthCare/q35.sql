-- 35. Get the total number of cities for each state available.

--SELECT state, COUNT(DISTINCT city) AS total_cities
--FROM addressinfo
--GROUP BY state;

SELECT a.state ,
(select count(m.member_id) from memberinfo m where m.member_id = a.memberinfo_member_id and m.gender='0') as  Male_Count,
(select count(m.member_id) from memberinfo m where m.member_id = a.memberinfo_member_id and m.gender='1') as  Female_Count
from addressinfo a
GROUP BY a.state
ORDER BY a.state;