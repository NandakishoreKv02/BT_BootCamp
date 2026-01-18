# Lab 5 Tasks

## Task 1: The Immutable Data anchor
- Define `ClinicalRecord`.
- `__init__(self, mrn, name)`:
  - Store `self.__mrn = mrn`.
  - Store `self._name = name`.

## Task 2: Implement MRN Property
- Create the `@property` for `mrn`.
- Ensure NO setter exists for `mrn`.

## Task 3: Implement Name Property
- Create `@property` and `@name.setter` for `name`.
- In the setter, ensure the new name is not empty.

## Task 4: The Audit Test
In `main()`:
1. Create a record.
2. Change the name.
3. Use a `try-except` block to show that `record.mrn = "NEW-123"` results in an `AttributeError`.
