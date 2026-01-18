# Lab 2 Tasks

## Task 1: Create the Component
Create a class `Scalpel`.
- `__init__(self)`: Set `self.sharpness = 100`.

## Task 2: Implement Composition
Create a class `SurgicalKit`.
- `__init__(self, kit_id)`:
  - Store `self.kit_id`.
  - Create a new `Scalpel` object and assign it to `self.scalpel`.

## Task 3: Access the Internal Object
In `main()`:
1. Create a `SurgicalKit`.
2. Access the scalpel inside the kit to print its sharpness.
3. Show that if you destroy the kit (conceptual), the scalpel is also gone because it was created inside the kit's constructor.
