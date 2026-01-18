# Lab 5 Tasks

## Task 1: The Robust Constructor
- Define `SurgicalCase`.
- `__init__(self, patient_name, procedure, surgeon="TBD", room=0)`:
  - Map arguments to attributes.
  - Calculate `self.complexity_score = len(procedure)`.

## Task 2: Standard Case
In `main()`:
1. Create a case for "John Doe" using only mandatory arguments.

## Task 3: Comprehensive Case
In `main()`:
1. Create a case for "Jane Doe" specifying all optional arguments.
2. Use keyword arguments (e.g., `surgeon="Dr. House"`) for readability.

## Task 4: Reporting
Print the summary for both cases showing all attributes and the automatically calculated complexity score.
