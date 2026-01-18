-- 2. Get all the predictions for the day.

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE;

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-22';