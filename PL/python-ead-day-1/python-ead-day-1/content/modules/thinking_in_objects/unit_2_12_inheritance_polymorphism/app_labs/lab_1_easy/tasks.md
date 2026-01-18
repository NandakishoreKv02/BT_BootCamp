# Lab 1 Tasks

## Task 1: Define Parent
- Create `Person` class.
- `__init__(self, name)`: Set `self.name`.

## Task 2: Define Child
- Create `StaffMember` inheriting from `Person`.
- `__init__(self, name, employee_id)`:
  - Assign `self.name` and `self.employee_id`. (Note: use super() if you want, but mandatory assignment is required).

## Task 3: Verification
In `main()`:
1. Create a `StaffMember`.
2. Print the name and ID.
3. Use `isinstance(obj, Person)` to verify the relationship.
