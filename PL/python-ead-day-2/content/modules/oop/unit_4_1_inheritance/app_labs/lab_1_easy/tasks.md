# Lab 1 Tasks

## Task 1: Create Base Class `Staff`
- Define `Staff` with an `__init__` method.
- It should accept `name` (str) and `employee_id` (str).
- Store these as instance attributes.
- Add a method `clock_in()` that returns `"Staff [ID] clocked in"`.

## Task 2: Create Subclass `MedicalStaff`
- Define `MedicalStaff` that inherits from `Staff`.
- Its `__init__` should accept `name`, `employee_id`, and `license_number`.
- Use `super().__init__` to handle name and ID.
- Store `license_number` as an instance attribute.

## Task 3: Verify Inheritance
- Instantiate a `MedicalStaff` member.
- Check that they have `name`, `employee_id`, and `license_number`.
- Call `clock_in()` on the `MedicalStaff` instance to prove method inheritance works.
