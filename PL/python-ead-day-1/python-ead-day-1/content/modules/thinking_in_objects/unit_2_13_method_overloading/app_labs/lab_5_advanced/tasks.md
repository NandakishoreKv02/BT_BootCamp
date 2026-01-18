# Lab 5 Tasks

## Task 1: Type Checking Logic
- Define `DiagnosticCenter`.
- Implement `fetch_details(self, query)`.
- Use `isinstance(query, int)` to handle IDs.
- Use `isinstance(query, dict)` to handle filters.

## Task 2: Invalid Inputs
- Add an `else` block to raise `TypeError` for other types (like `str` or `list`).

## Task 3: Reporting
In `main()`:
1. Call with an integer.
2. Call with a dictionary.
3. Call with a list (wrapped in `try-except`) and print the error message.
