# Lab 6 Tasks

## Task 1: The Static Store
- Define `MedicalStaff`.
- Define `ALL_STAFF = []` as a static class variable.

## Task 2: The Polymorphic Factory
- Implement `@classmethod spawn_from_name(cls, name)`.
- **Constraint**: Must use `cls(name)` to return the correct subtype when inherited.

## Task 3: Automatic Registration
- In `MedicalStaff.__init__`:
  - Append the current instance (`self`) to `MedicalStaff.ALL_STAFF`.

## Task 4: Subclassing
- Define `Physician` inheriting from `MedicalStaff`.

## Task 5: Integration
In `main()`:
1. Create a `MedicalStaff` object via factory.
2. Create a `Physician` object via factory.
3. Print the length of the registry.
4. Loop through the registry and print the name and type of each member.
