# Lab 1 Tasks

## Task 1: Create the Part
Create `Bed` class with `__init__(self, num)`.

## Task 2: Implement 1:N Composition
Create `HospitalWard` class.
- `__init__(self, name, size)`:
  - Store `self.name`.
  - Create a list `self.beds`.
  - Loop from 1 to `size` and append `Bed(i)` to the list.

## Task 3: Test the Connection
In `main()`:
1. Create a "General Ward" with 15 beds.
2. Print the ward name and the length of its beds list.
