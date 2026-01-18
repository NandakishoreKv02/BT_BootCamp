# Lab 2 Tasks

## Task 1: The Bed Blueprint
Create a class named `Bed`.
- `__init__(self, model)`: Set `self.model` to the argument and `self.is_occupied` to `False`.

## Task 2: Create Identical Twins
In `main()`:
- Create `bed_a = Bed("Model-X")`.
- Create `bed_b = Bed("Model-X")`.

## Task 3: Compare Identity
- Print the result of `bed_a is bed_b`.
- Print the results of `id(bed_a)` and `id(bed_b)`.
- Explain (in a comment or print) why they have different IDs even though their models are the same.
