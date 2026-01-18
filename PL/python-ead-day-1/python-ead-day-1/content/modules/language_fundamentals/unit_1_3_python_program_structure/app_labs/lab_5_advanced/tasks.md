# Lab 5: Hospital Department Manager - Tasks

## Task 1: Analyze Data Structure
Review the `HOSPITAL_DATA` constant in `starter_code.py`. It is a dictionary where:
- Keys are Department Names (str)
- Values are dictionaries of Wards
    - Ward Keys are Ward Names (str)
    - Ward Values are dicts with `occupied` and `total` integers.

## Task 2: Implement generate_report
Create logic to iterate through this structure:
- Initialize `total_beds` and `total_occupied` to 0.
- Iterate Departments.
- Iterate Wards.
- Sum up `total` and `occupied`.
- Return `{"total_beds": ..., "total_occupied": ..., "occupancy_rate": ...}`
    - `occupancy_rate` should be a float rounded to 2 decimals.
    - Handle division by zero if total beds is 0.

## Task 3: Refactor with Helper Function (Recommended)
Try to split the logic:
- `get_ward_stats(ward_data)` -> returns tuple `(occupied, total)`
- `generate_report` calls this helper.
**Why**: Reduces indentation depth. This is a best practice.

## Task 4: Main Guard verification
Add a main guard to print the report for the provided test data.
