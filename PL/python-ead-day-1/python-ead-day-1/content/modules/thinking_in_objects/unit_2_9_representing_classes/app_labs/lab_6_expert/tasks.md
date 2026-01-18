# Lab 6 Tasks

## Task 1: The Complex Constructor
- Define `HospitalDepartment`.
- `__init__(self, name, floor)`:
  - Store `name` and `floor`.
  - Initialize `self.sub_units = []`.
  - **Logic**: If "ER" or "ICU" is in the name, set `self.urgency = "High"`. Otherwise, set it to "Normal".

## Task 2: Recursive Association
- Implement `add_subunit(self, dept_obj)`.
- Append the new department object to the list.

## Task 3: The Reporting View
- Implement `summary(self)`.
- Print the main department's name and urgency.
- Loop through `sub_units` and print their names/urgencies with an indent.

## Task 4: Construction
In `main()`:
1. Create "Emergency Room" (Floor 1).
2. Create "Triage" (Floor 1) and "Trauma 1" (Floor 1).
3. Add Triage and Trauma as sub-units to Emergency.
4. Call `summary()` on the Emergency department.
