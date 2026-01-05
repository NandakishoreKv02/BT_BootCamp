-- 16. Get wearable device data details for cardio IDs between CID100 and CID200.

SELECT *
FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';