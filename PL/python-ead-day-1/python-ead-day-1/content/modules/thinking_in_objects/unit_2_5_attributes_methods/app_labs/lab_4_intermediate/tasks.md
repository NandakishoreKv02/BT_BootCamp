# Lab 4 Tasks

## Task 1: Clean the Blueprint
Define a class `LabReport`.
- `__init__(self, patient_id)`: Initialize with `self.patient_id` and an empty dictionary `self.results`.

## Task 2: Cohesive Methods
- Define `add_result(self, test_name, value)`: Adds the test and value to the dictionary.
- Define `is_abnormal(self)`:
  - If "Glucose" is > 125, return `True`.
  - Else return `False`.

## Task 3: The Audit (Comment)
In a comment at the top of your `starter_code.py`, list at least two methods that SHOULD NOT be in this class based on the "Low Cohesion" problem statement (e.g., `send_marketing_email`, `calculate_parking_fees`).

## Task 4: Run the Report
In `main()`:
1. Create a lab report for Patient 505.
2. Add a Glucose result of 140.
3. Print the abnormal status.
