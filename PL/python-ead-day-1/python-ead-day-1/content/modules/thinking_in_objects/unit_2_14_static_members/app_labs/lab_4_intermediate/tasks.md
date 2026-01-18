# Lab 4 Tasks

## Task 1: Basic Constructor
- Define `Patient`.
- `__init__(self, name, age, blood_type)`.

## Task 2: The Factory Method
- Use the `@classmethod` decorator.
- Implement `from_legacy_string(cls, data_line)`.
- Use `.split(" | ")` to parse the string.
- Call `cls(name, age, type)` and return the result.

## Task 3: Integration
In `main()`:
1. Create a patient using the standard constructor.
2. Create a patient using `Patient.from_legacy_string("Bob | 45 | O+")`.
3. Print details for both.
