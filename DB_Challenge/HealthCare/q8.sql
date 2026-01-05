-- 8. Get the X-ray details of Ajay whose cardio test was done on 26th of Jan 2019.

SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'ajay'
  AND DATE(c.date) = '2019-01-26';