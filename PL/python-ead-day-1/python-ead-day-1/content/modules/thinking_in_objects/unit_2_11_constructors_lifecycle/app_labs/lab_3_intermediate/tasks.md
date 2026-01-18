# Lab 3 Tasks

## Task 1: Sentinel Parameter
- Define `PharmacyOrder`.
- Implement `__init__(self, medications=None)`.

## Task 2: Initialization Logic
- Inside the constructor:
  - If `medications` is `None`, set `self.medications = []`.
  - Otherwise, set `self.medications = medications`.

## Task 3: Support Method
- Add `add_drug(self, drug)` to append to the list.

## Task 4: Independence Test
In `main()`:
1. Create `order1` and `order2` using no arguments.
2. Add "Aspirin" to `order1`.
3. Print both medication lists.
