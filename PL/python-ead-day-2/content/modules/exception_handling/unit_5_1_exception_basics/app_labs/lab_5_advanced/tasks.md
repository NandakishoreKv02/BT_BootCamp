# Lab 5 Tasks

## Task 1: The Parser
- Implement `parse_record(raw_string)`.
- Expected format: `"ID:101;AGE:45"`.
- Split by `";"` first, then by `":"`.

## Task 2: Specific Handling
- Catch `ValueError` during integer conversion -> return "Invalid Number".
- Catch `IndexError` during splitting (if `":"` is missing) -> return "Invalid Format".

## Task 3: The Else Block
- Use `else` to construct the dictionary `{'id': ..., 'age': ...}`.
- Return the dictionary on success.
- If any error occurs, returning the error string is fine for this lab.
