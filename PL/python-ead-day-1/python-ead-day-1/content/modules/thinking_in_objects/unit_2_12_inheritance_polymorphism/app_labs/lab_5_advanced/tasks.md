# Lab 5 Tasks

## Task 1: Root Class
- Define `StaffMember`.
- `__init__(self, name)`.

## Task 2: Middle Class
- Define `Doctor(StaffMember)`.
- `__init__(self, name, license_id)`:
  - Call `super().__init__(name)`.
  - Store `license_id`.

## Task 3: Leaf Class
- Define `Surgeon(Doctor)`.
- `__init__(self, name, license_id, surgical_specialty)`:
  - Call `super().__init__(name, license_id)`.
  - Store `surgical_specialty`.

## Task 4: Verification
In `main()`:
1. Create a `Surgeon` instance.
2. Print all three inherited/own attributes.
