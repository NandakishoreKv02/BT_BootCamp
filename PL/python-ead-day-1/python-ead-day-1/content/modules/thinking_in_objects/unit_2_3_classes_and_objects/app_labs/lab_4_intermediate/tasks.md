# Lab 4 Tasks

## Task 1: The Doctor Entity
Create a class `Doctor` with `name` and `specialty`.

## Task 2: The Ward Container
Create a class `Ward`.
- `__init__(self, name)`: Set name and an empty list `doctors`.
- `assign_doctor(self, doc)`: Append the `doc` object to the list.
- `print_staff(self)`: Iterate through the `doctors` list and print each doctor's name and specialty.

## Task 3: Simulating the Hospital
In `main()`:
1. Create a `Ward` called "Pediatrics".
2. Create three `Doctor` objects.
3. Assign them to the ward using the `assign_doctor` method.
4. Call `print_staff()` to verify that the ward object correctly "contains" the doctor objects.
