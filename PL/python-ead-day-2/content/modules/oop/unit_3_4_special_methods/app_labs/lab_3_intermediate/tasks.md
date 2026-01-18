# Lab 3 Tasks: Priority Queue

## Task 1: Create TriagePatient (15 points)
- Attributes: patient_id, name, urgency (1-5, 1=critical)

## Task 2: Implement `__eq__` (20 points)
- Compare by patient_id
- Return NotImplemented for non-TriagePatient

## Task 3: Implement `__lt__` (25 points)
- Compare by urgency (lower = higher priority)
- Return NotImplemented for non-TriagePatient

## Task 4: Use @total_ordering (20 points)
- Apply decorator from functools
- This generates __le__, __gt__, __ge__

## Task 5: Test Sorting (20 points)
- Create list of patients with varying urgency
- Use sorted() to order by priority
- Verify critical patients come first
