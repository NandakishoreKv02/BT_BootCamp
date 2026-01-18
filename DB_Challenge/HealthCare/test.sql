-- identify high-risk heart attack patients by state and gender who meet all of the following conditions:
-- Diagnosed with a heart attack
-- Age > 45
-- Blood pressure ≥ 140
-- Cholesterol > 200
-- Wearable device slope = 2
-- Have undergone at least one X-ray
-- Have recorded at least one symptom
-- For each state and gender, return:
-- Number of high-risk patients
-- Average age
-- Average blood pressure
-- Average cholesterol

Pattern and approach to writing an SQL Statement
 
1. What do you need - Columns that you need as part of the output
 state name,gender,count of high-risk patients , avg age,average bloodpressure,average cholesterol

2. Where do you have the information that you need - Tables
3. Connections - Joins - How do you join the tables to get the information
4. Join Conditions
5. Other conditions apart from join
6. Aggregate function to be used
7. Group, Having
8. SubQuery and/or any other predicates
9. Order in which the informatio

select a.state, m.gender,count(DISTINCT m.member_id),avg(m.age),avg(b.bloodpressure),avg(b.serumcholesterol)
from memberinfo m 
join addressinfo a on a.memberinfo_member_id=m.member_id
join cardiodiagnosis c on c.memberinfo_member_id = m.member_id
join bloodtest b on b.cardiodiagnosis_cardio_id = c.cardio_id
join wearabledevicedata w on w.cardiodiagnosis_cardio_id = c.cardio_id
join xray x on x.cardiodiagnosis_cardio_id = c.cardio_id
join symptom s on s.cardiodiagnosis_cardio_id = c.cardio_id
where m.age>45 and b.bloodpressure>=140 and w.slope =2
group by a.state,m.gender
order by a.state,m.gender;