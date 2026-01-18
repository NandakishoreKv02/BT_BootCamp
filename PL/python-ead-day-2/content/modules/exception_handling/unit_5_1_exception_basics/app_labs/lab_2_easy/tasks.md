# Lab 2 Tasks

## Task 1: Safe Getter
- In `starter_code.py`, implement `get_record_field`.
- It takes `database`, `record_id`, and `field_name`.
- Attempt to return `database[record_id][field_name]`.

## Task 2: Handling Missing Records
- Wrap the access in `try-except`.
- If `KeyError` occurs, catch it.
- Return the string `"Data Not Found"`.

## Task 3: Testing
- Verify it works for existing data.
- Verify it returns the error string for missing IDs or missing fields.
