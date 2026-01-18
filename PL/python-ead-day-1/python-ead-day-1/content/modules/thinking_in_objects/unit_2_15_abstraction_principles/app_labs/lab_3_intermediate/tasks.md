# Lab 3 Tasks

## Task 1: Identify Responsibilities
- Look at the `PatientBillingOfficer` in the starter code.
- Note the three jobs: Data storage, Calculation, and UI Rendering.

## Task 2: Implement SRP Classes
- Create `PatientProfile` (Data).
- Create `CostCalculator` (Calculation).
- Create `StatementRenderer` (UI).

## Task 3: Integration
In `main()`:
1. Create a profile with services `[{"name": "Consult", "price": 100}, {"name": "Lab", "price": 350}]`.
2. Use the calculator to get the total.
3. Use the renderer to print the final statement.
