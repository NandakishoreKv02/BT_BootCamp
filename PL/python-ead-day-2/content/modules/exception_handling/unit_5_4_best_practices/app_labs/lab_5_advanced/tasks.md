# Lab 5 Tasks

## Task 1: The Integrity Validator
- Implement `validate_prescription(data)`.
- It should check if `dose` is a positive number and `drug` is a non-empty string.
- Return a list of error strings. If empty, data is clean.

## Task 2: Core Engine
- Implement `calculate_schedule(dose, frequency)`.
- It performs `dose / frequency`.

## Task 3: The Shield
- Implement `secure_scheduler(data)`.
- First, call `validate_prescription`.
- If errors exist, return `{"status": "rejected", "errors": errors}`.
- If clean, wrap `calculate_schedule` in a specific `try-except ZeroDivisionError`.
- Return `{"status": "success", "result": result}`.
