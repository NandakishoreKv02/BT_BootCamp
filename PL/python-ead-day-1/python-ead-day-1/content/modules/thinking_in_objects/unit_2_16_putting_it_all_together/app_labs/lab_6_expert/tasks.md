# Lab 6 Tasks

## Task 1: Core Classes
- Define `Patient` (Encapsulate balance).
- Define `Doctor`.
- Define `Department`.

## Task 2: Interaction Logic
- implement `Department.assign_doctor(specialty)`.
- Implement `Doctor.treat(patient, procedure, cost)`.
  - This calls `patient.add_procedure(...)` and `patient.add_charge(...)`.

## Task 3: Static Utility
- Implement `BillingSystem.generate_invoice(patient)`.

## Task 4: Grand Simulation
In `main()`:
1. Setup a Department ("Cardiology") with 2 doctors.
2. Create a Patient.
3. Simulate the flow: Assign -> Treat -> Bill.
