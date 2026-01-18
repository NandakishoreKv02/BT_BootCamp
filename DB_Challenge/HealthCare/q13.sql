-- 13. Get all symptom details whose cardio ID is CID250 and CID300.

SELECT *
FROM symptom
WHERE cardiodiagnosis_cardio_id IN ('cid250', 'cid300');