# Lab 3 Tasks

## Task 1: Initialize the Prescription
Create a class `Prescription`.
- `__init__(self, drug_name)`: Initialize `dose=0`, `unit=""`, and `freq=""`.

## Task 2: Implement the Signature
Define `set_instructions(self, dose, unit, frequency)`.
- Update the three instance attributes.
- Return a string: `"Take [dose][unit], [frequency]."`

## Task 3: Trigger the Pharmacy Label
In `main()`:
1. Create a prescription for "Insulin".
2. Call `set_instructions(10, 'units', 'Before meals')`.
3. Print the returned label string.
