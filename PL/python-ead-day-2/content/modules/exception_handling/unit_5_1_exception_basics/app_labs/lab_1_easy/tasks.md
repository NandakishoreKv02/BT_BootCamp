# Lab 1 Tasks

## Task 1: Safe Parsing Helper
- In `starter_code.py`, implement `safe_int_conversion(value)`.
- Use `try-except ValueError` to attempt conversion.
- Return the integer if successful, `None` if it fails.

## Task 2: Process Intake Function
- Implement `process_intake(raw_data)`.
- It receives a dictionary like `{"age": "25", "weight": "70.5"}`.
- Use the helper to convert fields.
- Also handle `weight` (float conversion).

## Task 3: Error Reporting
- If `age` is invalid, add "Invalid Age" to an `errors` list.
- If `weight` is invalid, add "Invalid Weight" to the list.
- Return `(clean_data, errors)`. `clean_data` should be `None` if there are errors.
