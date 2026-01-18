# Lab 1 Tasks

## Task 1: Define the Entity
Create `PatientRecord`.
- `__init__(self, name, symptoms)`: Store the values.

## Task 2: Define the Actor
Create `TriageNurse`.
- `__init__(self, nurse_name)`: Store the name.

## Task 3: Implement the Verb
Inside `TriageNurse`, define `calculate_urgency(self, patient_obj)`:
- If the patient has "Chest Pain" in symptoms, return 5.
- If the patient has "Cough", return 2.
- Else return 1.

## Task 4: Integration
In `main()`:
1. Create a nurse.
2. Create a patient with "Chest Pain".
3. Call the nurse's method to calculate the score.
4. Print the result.
