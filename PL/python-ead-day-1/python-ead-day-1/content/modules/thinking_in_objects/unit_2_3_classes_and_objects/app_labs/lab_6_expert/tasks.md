# Lab 6 Tasks

## Task 1: Defining the Actors
- Create `Doctor`: `__init__(self, name)` and `self.patient_list = []`.
- Create `Patient`: `__init__(self, name, mrn)` and `self.doctor = None`.

## Task 2: Implementing Interaction
Define a function `link_doctor_patient(doctor_obj, patient_obj)`:
- Assign `doctor_obj` to `patient_obj.doctor`.
- Append `patient_obj` to `doctor_obj.patient_list`.

## Task 3: The Summary Method
Add a method `get_summary(self)` to the `Doctor` class:
- Returns a string: `"Dr. [Name] - [Count] Patients"`.

## Task 4: Hospital Run
In `main()`:
1. Create `dr_strange = Doctor("Strange")`.
2. Create patients "Tony" and "Stephen".
3. Use `link_doctor_patient` to connect them.
4. Print the doctor's summary.
5. Iterate through `dr_strange.patient_list` and print each patient's name and MRN.
