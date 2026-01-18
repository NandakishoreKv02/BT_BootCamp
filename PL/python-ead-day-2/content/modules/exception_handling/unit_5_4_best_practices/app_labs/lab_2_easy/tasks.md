# Lab 2 Tasks

## Task 1: Analyze the Bloat
- View `calculate_avg_vitals_bloated`.
- It wraps 5 lines of code in `except Exception`.

## Task 2: Narrow the Scope
- Create `calculate_avg_vitals_clean(total, count)`.
- Move the `logging` and `return` logic OUTSIDE of the `try` block.
- Only the division should be inside `try`.

## Task 3: Specific Catching
- Catch `ZeroDivisionError` specifically.
- Return `0` instead of a generic error string.
