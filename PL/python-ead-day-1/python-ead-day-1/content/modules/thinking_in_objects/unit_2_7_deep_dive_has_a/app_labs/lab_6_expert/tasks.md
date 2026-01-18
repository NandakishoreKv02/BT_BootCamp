# Lab 6 Tasks

## Task 1: The Composition Tiers
- Create `Medication` (`drug_name`).
- Create `Patient`.
  - Initialize `self.meds = []` and `self.doctors = []`.
  - `add_med(self, drug)`: Create `Medication(drug)` and append (**Composition**).
- Create `Clinic`.
  - Initialize `self.patients = []`.
  - `register_new_patient(self, name)`: Create `Patient(name)` and append (**Composition**).

## Task 2: The Aggregation Layer
- Create `Doctor` (`name`).
  - Initialize `self.patients = []`.
  - `assign_to_patient(self, patient_obj)`: Perform bidirectional sync with the patient objects.

## Task 3: The Integrated Test
In `main()`:
1. Create a Clinic "City General".
2. Create a Doctor "Dr. Smith".
3. Register Patient "John" at the clinic.
4. Add two medications to John's chart.
5. Assign Dr. Smith to John.
6. Print the full hierarchy: Clinic -> Patient -> [Meds] AND [Doctor].
