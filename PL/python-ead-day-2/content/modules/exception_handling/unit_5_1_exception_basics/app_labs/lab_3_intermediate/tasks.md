# Lab 3 Tasks

## Task 1: The Calculator Function
- Implement `calculate_dose_per_intake(total_mg, frequency)`.
- Inside `try`, perform `result = total_mg / frequency`.

## Task 2: Handling Zero Division
- Add `except ZeroDivisionError`.
- Return `None` and print "Error: Frequency cannot be zero".

## Task 3: Handling Invalid Input
- Add `except (TypeError, ValueError)`.
- Return `None` and print "Error: Invalid inputs".

## Task 4: The Else Clause
- Add `else:` block.
- Return `round(result, 2)`.
