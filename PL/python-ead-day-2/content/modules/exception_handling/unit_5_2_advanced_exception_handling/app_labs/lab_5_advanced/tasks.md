# Lab 5 Tasks

## Task 1: Safe Open
- Implement `process_patient_file(path)`.
- Use `with open(path, 'r')` to read the file.
- Handle `FileNotFoundError` by returning `[]`.

## Task 2: Robust Parsing
- Iterate over lines. Each line is an integer age (e.g., "45").
- Convert to int.
- Wrap conversion in `try-except ValueError`.
- If valid, add to list.
- If invalid, ignore that line.

## Task 3: Return
- Return list of valid ages.
