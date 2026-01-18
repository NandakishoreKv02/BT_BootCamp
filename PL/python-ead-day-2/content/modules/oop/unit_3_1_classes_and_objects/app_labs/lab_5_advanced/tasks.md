# Lab 5 Tasks: Object Identity and Equality

## Task 1: Create Identical Data Objects
- Open `starter_code.py`.
- Create `record1` with name="John Smith" and id=101.
- Create `record2` with name="John Smith" and id=101.

## Task 2: Create an Alias
- Create `record3` and assign `record1` to it.

## Task 3: Implement Identity/Equality Check
- Implement a function `compare_records(r1, r2)` that returns a tuple: `(is_same_object, has_same_data)`.
- `is_same_object`: Should be `True` if `r1 is r2`.
- `has_same_data`: Should be `True` if `r1.name == r2.name` and `r1.id == r2.id`.
