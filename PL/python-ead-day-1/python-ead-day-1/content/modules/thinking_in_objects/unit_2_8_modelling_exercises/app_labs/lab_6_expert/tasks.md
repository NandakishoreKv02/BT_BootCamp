# Lab 6 Tasks

## Task 1: Identify the Split
Analyze the provided (messy) class and identify the three logical entities.

## Task 2: Implement the Refined Modules
- Create `PatientRegistry`: Has a dictionary of `mrn: name`.
- Create `ClinicalNotebook`: Has a dictionary of `mrn: list_of_vitals`.
- Create `BillingModule`: Has a dictionary of `mrn: total_due`.

## Task 3: The Coordinator
Create `EHRPlatform`.
- In `__init__`, create instances of all three modules (**Composition**).
- Implement a method `process_new_patient(self, name, mrn, initial_vitals, fee)`:
  - Call `registry.register(name, mrn)`.
  - Call `notebook.add_entry(mrn, initial_vitals)`.
  - Call `billing.apply_fee(mrn, fee)`.

## Task 4: Run the Multi-Module process
In `main()`:
1. Initialize the `EHRPlatform`.
2. Process two different patients.
3. Print a summary showing that the data is stored in the separate modules, not the main platform.
