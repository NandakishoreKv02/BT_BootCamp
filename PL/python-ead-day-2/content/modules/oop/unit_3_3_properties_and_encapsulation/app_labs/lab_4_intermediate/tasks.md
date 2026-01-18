# Lab 4 Tasks: Access Control

## Task 1: Public Attributes (20 points)
Define a `PatientRecord` class with public attributes `name` and `gender`. These should be accessible directly.

## Task 2: Protected Attributes (20 points)
Add a protected attribute `_medical_conditions` (list).
- Provide a method `add_condition(condition)` to append to this list.
- Provide a property `conditions` that returns a copy of the list (to prevent direct modification of the internal list).

## Task 3: Private Attributes (30 points)
Add private attributes `__ssn` and `__insurance_id`.
- These are sensitive and should utilize double underscore naming.
- Provide a read-only property `ssn_last_4` that returns only the last 4 digits (e.g., "***-**-1234").
- Provide a write-only setter for `insurance_id` (or a method `update_insurance`) to update it, but no public getter.

## Task 4: Access Level Verification (15 points)
Implement a method `get_access_report()` that returns a dictionary indicating which fields are set, without revealing values of private fields.

## Task 5: Name Mangling Demo (15 points)
Create a method `_internal_debug()` that accesses `__ssn` directly. Note how outside the class, `obj.__ssn` fails, but `obj._PatientRecord__ssn` works (demonstrating name mangling).
