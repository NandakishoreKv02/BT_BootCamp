-- 3. Get all the predictions for the day and sort them based on the highest probability percentage at the top.

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20'  
ORDER BY cardioarrestdetected DESC;