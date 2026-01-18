# Lab 4 Tasks

## Task 1: The Data Objects
- Create `BloodSample` (`sample_id`).
- Create `LabResult` (`value`, `status`).

## Task 2: Implement the Dependency Tool
Create `Analyzer` class.
- `__init__(self, model_name)`: Store name.
- `process(self, sample_obj)`:
  - Print that it's processing the sample ID.
  - Return a new `LabResult("Normal", "Verified")`.

## Task 3: The Pipeline Setup
In `main()`:
1. Create a "Hemoglobin-X" analyzer.
2. Create a blood sample.
3. Pass the sample to the analyzer's process method.
4. Print the details of the returned result object.
