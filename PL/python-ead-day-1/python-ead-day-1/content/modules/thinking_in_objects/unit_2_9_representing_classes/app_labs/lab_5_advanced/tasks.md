# Lab 5 Tasks

## Task 1: The Blueprint
Define `Physician` with `dr_id`, `name`, and an empty `assigned_patients` list in the constructor.

## Task 2: State Logic
Implement `assign_patient(self, patient_name)`:
- Append the name to the instance's list.

## Task 3: The Factory Loop
In `main()`:
1. Create an empty list called `registry`.
2. Use a `for` loop to create 5 `Physician` objects.
3. Append each to the `registry`.

## Task 4: The Independence Check
1. Access the first doctor in the registry (`registry[0]`).
2. Assign them "Patient A".
3. Print the patient list for the first and second doctor to show they are different.
