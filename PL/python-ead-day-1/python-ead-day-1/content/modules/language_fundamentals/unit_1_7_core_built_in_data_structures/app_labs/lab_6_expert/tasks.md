# Lab 6: Hospital Hierarchy Mapper - Tasks

## Task 1: Registration
In `register_doctor`:
- If `dept` is not in `registry`, add it as an empty dictionary.
- If `doctor` is not in that department's dictionary, add them as an empty set.
- Add the `specialty` to the doctor's set.

## Task 2: Doctor Retrieval
In `get_dept_doctors`, return a list of keys (doctor names) for the specified department. If the department doesn't exist, return an empty list.

## Task 3: Meta-Analysis
In `get_unique_specialties_for_dept`:
- Create an empty set `all_specs`.
- Iterate through all doctors in the department.
- Use the `.union()` method or `|=` operator to combine the doctor's specialties into `all_specs`.
- Return `all_specs`.
