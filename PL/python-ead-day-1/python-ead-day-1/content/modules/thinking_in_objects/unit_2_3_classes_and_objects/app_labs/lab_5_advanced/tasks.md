# Lab 5 Tasks

## Task 1: The Prescription Definition
Define a class `Prescription`.
- `__init__(self, drug, dose)`: Set drug, dose, and `self.status = "PENDING"`.

## Task 2: Implementing the Workflow
Create the following methods with logic checks:
- `fill(self)`: 
  - If status is "PENDING", update to "FILLED" and return `True`.
  - Else return `False`.
- `dispense(self)`:
  - If status is "FILLED", update to "DISPENSED" and return `True`.
  - Else return `False`.
- `cancel(self)`:
  - If status is NOT "DISPENSED", update to "CANCELLED" and return `True`.
  - Else return `False`.

## Task 3: Simulating Failures
In `main()`:
1. Create a prescription for "Aspirin".
2. Attempt to `dispense()` it immediately. (Should fail).
3. `fill()` it. (Should pass).
4. `dispense()` it. (Should pass).
5. Attempt to `cancel()` it. (Should fail because it is already dispensed).
