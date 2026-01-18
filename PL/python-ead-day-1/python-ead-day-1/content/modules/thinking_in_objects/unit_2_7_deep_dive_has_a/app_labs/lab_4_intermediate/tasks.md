# Lab 4 Tasks

## Task 1: Create the Component classes
- `MedicalHistory`: Stores `notes`.
- `Doctor`: Stores `name`.

## Task 2: Implement the Complex Hub
Create `PatientFile`.
- `__init__(self, patient_name)`:
  - Create a new `MedicalHistory()` and store in `self.history` (**Composition**).
  - Set `self.reviewer = None` (**Aggregation**).
- `assign_doctor(self, doctor_obj)`: Set `self.reviewer = doctor_obj`.

## Task 3: The Audit Demo
In `main()`:
1. Create a Doctor "Dr. Wilson".
2. Create two Patient Files.
3. Assign Dr. Wilson to both.
4. Print the memory addresses of both patients' histories (they must be different).
5. Print the memory address of the reviewer for both (they must be the same).
