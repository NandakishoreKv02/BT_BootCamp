# Lab 4 Tasks

## Task 1: Create the Sub-Entity
Define the `Vitals` class.
- `__init__(self, sys, dia, temp)`: Store clinical data.
- `is_fever(self)`: Return `True` if `temp > 100.4`.

## Task 2: Update the Main Entity
Define the `Patient` class.
- `__init__(self, name)`: Set the name and initialize `self.vitals = None`.
- `update_vitals(self, vitals_obj)`: Assign the `vitals_obj` to `self.vitals`.

## Task 3: Refined Interaction
In `main()`:
1. Create a `Patient` called "John Doe".
2. Create a `Vitals` object with a temperature of 101.5.
3. Link the vitals to the patient.
4. Print the patient's name and a message if they have a fever.
