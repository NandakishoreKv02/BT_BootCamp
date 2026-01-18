# Lab 3 Tasks

## Task 1: Initialize Protected Data
- Define `MedicationRequest`.
- `__init__(self, dose)`: Store `self._dose = dose`.

## Task 2: Implement the Interface
- Create `@property` for `dose`.
- Create `@dose.setter` for `dose`.

## Task 3: The Validation logic
In the setter:
1. Check if the value is between 1 and 500.
2. If yes, update `self._dose = value`.
3. If no, print "Error: Invalid Dose".

## Task 4: Transaction Test
In `main()`:
1. Create a request for 100mg.
2. Try to update it to 600mg.
3. Print the final dose to verify it is still 100mg.
