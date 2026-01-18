# Lab 3 Tasks

## Task 1: Identify and Extract Entities
Create the `Patient` class.
- Move `name` and `id` from the old app to this class.

## Task 2: Implement the Billing Logic
Create `BillingEngine`.
- Define `calculate(self, days, rate)`: Returns `days * rate`.

## Task 3: Implement the Ward Manager
Create `Ward`.
- Store a `name`.
- Define `assign_bed(self, patient_obj, bed_number)`: Return a formatted string linking the patient to a bed.

## Task 4: Successful Collaboration
In `main()`:
1. Create a `Patient` object.
2. Create a `Ward` and a `BillingEngine`.
3. Use the `Ward` to assign a bed.
4. Use the `BillingEngine` to get a total cost.
5. Print the final combined summary.
