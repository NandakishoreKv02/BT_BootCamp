# Lab 6 Tasks

## Task 1: Design Data Structures
Decide on your dictionary keys.
- Patient: `id`, `name`, `status` ("Admitted"/"Discharged"), `assigned_doctor_id` (optional).
- Doctor: `id`, `name`, `assigned_patients` (list of IDs).

## Task 2: Constructor Functions
- `create_patient(id, name)`
- `create_doctor(id, name)`

## Task 3: Interaction Logic
- `assign_doctor(doctor_dict, patient_dict)`:
    - Add patient ID to doctor's list.
    - Set patient's assigned doctor ID.
- `discharge_patient(patient_dict)`:
    - Set status to "Discharged".
    - (Optional) Remove from Doctor's list (cleaning up relationships).

## Task 4: Reporting
- `print_hospital_status(doctors, patients)`:
    - Loop through doctors, print their patients.
    - Loop through unassigned patients.

## Task 5: Full Migration
- In `main()`, recreate the scenario from the "Bad Code" using your new functions.
