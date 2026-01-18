# Lab 1 Tasks

## Task 1: Define Exception
- Define `PatientNotFound` inheriting from `Exception`.

## Task 2: Lookup
- Implement `get_patient(db, patient_id)`.
- If `patient_id` not in `db`, raise `PatientNotFound(f"ID {patient_id} missing")`.

## Task 3: Usage
- Create a `db` dictionary.
- Verify catching `PatientNotFound` works.
