# Lab 2 Tasks

## Task 1: The Components
Create `IDCard` with `__init__(self, number)`.

## Task 2: The Base Class (Composition)
Create `HospitalStaff`.
- `__init__(self, name, role, card_num)`:
  - Store name and role.
  - Create a new `IDCard` using `card_num` (**Composition**).

## Task 3: The Specialized Class (Inheritance)
Create `Physician`.
- Inherit from `HospitalStaff`.
- `__init__(self, name, card_num, specialty)`:
  - Call `super().__init__` with the name, "Physician", and the card number.
  - Store specialty.
