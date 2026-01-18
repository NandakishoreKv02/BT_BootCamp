# Lab 6 Tasks

## Task 1: Conditional Constructor
- Define `PatientProfile`.
- `__init__(self, name, data_source, ehr_id=None)`:
  - Store `name` and `data_source`.
  - **Validation**: If `data_source == "EHR"` and `ehr_id` is `None`, raise `ValueError("EHR source requires an ID")`.
  - Store `self.ehr_id = ehr_id`.

## Task 2: Standard Profiles
In `main()`:
1. Create a "Manual" profile for "Bob".
2. Create an "EHR" profile for "Alice" with ID 999.

## Task 3: Error Handling
In `main()`:
1. Try to create an "EHR" profile for "Charlie" without an ID.
2. Wrap it in a `try-except` block to catch and print the error message.

## Task 4: Reporting
Display all created profiles or print the handled error message.
