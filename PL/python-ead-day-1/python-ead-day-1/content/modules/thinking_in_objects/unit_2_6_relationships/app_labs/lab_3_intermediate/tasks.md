# Lab 3 Tasks

## Task 1: Create the Data Entities
Create `Patient` (`name`) and `Prescription` (`drug`).

## Task 2: Implement the Dependency
Create a class `MedicationDispenser`.
- Define a method `dispense_to(self, patient, prescription)`.
- Inside the method:
  - Access `patient.name`.
  - Access `prescription.drug`.
  - Print a "Verification and Dispensing" message.

## Task 3: The Tool in Action
In `main()`:
1. Create one `MedicationDispenser`.
2. Create two different Patients and two different Prescriptions.
3. Use the **same** dispenser to process both patients sequentially.
