# Lab 1 Tasks

## Task 1: Identify and Create the Classes
- Create `SupplyItem` with `__init__(self, name, quantity)`.
- Create `Inventory` with `__init__(self)`.

## Task 2: Implement Composition
- In `Inventory`, initialize `self.items = []`.
- Implement `add_stock(self, name, qty)`:
  - Create a new `SupplyItem` object using the args.
  - Append it to the list.

## Task 3: Reporting
- Implement `show_inventory(self)` in the `Inventory` class to print all items.
