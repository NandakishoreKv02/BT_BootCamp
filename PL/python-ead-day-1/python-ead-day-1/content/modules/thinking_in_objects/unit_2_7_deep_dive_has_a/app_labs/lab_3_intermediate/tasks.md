# Lab 3 Tasks

## Task 1: Initialize the Entities
- `Doctor`: Initialize `self.patients = []`.
- `Patient`: Initialize `self.doctor = None`.

## Task 2: Implement Sync Method
In `Doctor`, implement `add_patient(self, patient_obj)`:
1. Append the patient to `self.patients`.
2. Set `patient_obj.doctor = self` (This is the bidirectional link).

## Task 3: Demonstration
In `main()`:
1. Create Dr. Gregory and Patient John.
2. Call `dr.add_patient(john)`.
3. Print `john.doctor.name` and check if john is in `dr.patients`.
