# Lab 1 Tasks

## Task 1: Create the Base Class
Create a class `Department`.
- `__init__(self, name, location)`: Store both values.

## Task 2: Implement Inheritance
Create a class `EmergencyDepartment`.
- It must inherit from `Department`.
- `__init__(self, name, location)`:
  - Use `super().__init__(name, location)` to initialize the base data.
  - Set `self.is_diverting = False`.

## Task 3: Demonstrate Specialization
In `main()`:
1. Create an instance of `EmergencyDepartment` called "ER-1" at "Building B".
2. Print its name and diversion status.
3. Change its status to `True` and print again.
