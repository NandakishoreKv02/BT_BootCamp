# Lab 2 Tasks

## Task 1: Update `Staff` Class
- Add a method `access_records()` to the existing `Staff` class.
- It should return `"Access Denied"`.

## Task 2: Override in `MedicalStaff`
- In `MedicalStaff`, define `access_records()` with the same signature.
- It should return `"Access Granted for [Name]"`.

## Task 3: Test Polymorphism
- Create a list containing both `Staff` and `MedicalStaff`.
- Loop through and print the result of `access_records()` for each.
- Observe different behaviors.
