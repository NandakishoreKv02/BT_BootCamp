# Lab 2 Tasks

## Task 1: The Entity
Create `Prescription`.
- `__init__(self, drug, dose)`: Store properties.

## Task 2: The Control
Create `DispensingLogic`.
- Define `verify(self, prescription)`: Return `True` if dose > 0, else `False`.

## Task 3: The Boundary
Create `PharmacyUI`.
- Define `display_result(self, prescription, is_valid)`:
  - Print `"PHARMACY TERMINAL: Processing [drug]..."`
  - Print `"Result: SUCCESS"` if valid, else `"Result: REJECTED"`.

## Task 4: Orchestration
In `main()`:
1. Create a prescription.
2. Initialize the Logic and UI classes.
3. Use Logic to verify the prescription.
4. Pass the result to UI to display.
