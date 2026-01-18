# Lab 6 Tasks

## Task 1: The Staff Hierarchy (Inheritance)
- Create `Staff` (`name`, `role`).
- Create `Physician` inheriting from `Staff`.

## Task 2: The Infrastructure (Composition)
- Create `Ward` (`name`).
- Create `Hospital`.
  - In `__init__`, create an "ICU" ward and a "General" ward (**Composition**).
  - Store them in a list `self.wards`.

## Task 3: The Staff-Ward Link (Aggregation)
- Modify `Ward` to accept a `nurse` object in a method `assign_nurse(self, nurse_obj)`.

## Task 4: The Tool Interaction (Dependency)
- Create `Analyzer` (`model_name`).
- In `Physician`, add a method `perform_analysis(self, analyzer, data)`.
  - It uses the analyzer to "process" the data.

## Task 5: The Full Simulation
In `main()`:
1. Create a Hospital.
2. Create a Nurse and assign them to the Hospital's ICU ward.
3. Create a Physician and an Analyzer.
4. Have the Physician perform an analysis on "Sample-X" using the analyzer.
