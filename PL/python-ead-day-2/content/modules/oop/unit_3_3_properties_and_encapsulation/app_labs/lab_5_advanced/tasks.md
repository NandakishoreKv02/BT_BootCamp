# Lab 5 Tasks: Advanced Validation

## Task 1: Date Logic (25 points)
Implement `start_date` and `end_date` properties.
- Ensure `end_date` cannot be set to before `start_date`.
- If `start_date` is moved to after `end_date`, raise `ValueError`.

## Task 2: Duration Calculation (20 points)
Implement `duration_days` property.
- Returns the number of days between start and end.
- This is read-only (no setter).
- Should calculate dynamically using `datetime` objects.

## Task 3: Dosage Safety (25 points)
Implement `daily_dosage_mg` property.
- Max safe dosage is 1000mg generally.
- Raise `ValueError` if negative or > 1000.

## Task 4: Total Calculation (15 points)
Implement `total_course_dosage_mg`.
- Computed as `duration_days * daily_dosage_mg`.

## Task 5: Status Check (15 points)
Implement `is_active` property.
- Returns `True` if today's date is between start and end (inclusive).
- Use `datetime.date.today()`.
