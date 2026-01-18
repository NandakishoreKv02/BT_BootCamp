# Lab 2 Tasks: Patient Registry

## Task 1: Create PatientRegistry (20 points)
- Initialize with empty `_patients` dict `{patient_id: patient}`
- Add method `register(patient)` to add patients

## Task 2: Implement `__len__` (25 points)
- Return count of registered patients
- `len(registry)` should work

## Task 3: Implement `__getitem__` (30 points)
- Accept patient_id as key
- Return patient object
- Raise KeyError if not found

## Task 4: Implement `__contains__` (25 points)
- Check if patient_id exists
- `"P001" in registry` should return True/False
