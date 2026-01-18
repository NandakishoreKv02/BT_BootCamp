# Lab 4: Data Cleaner - Tasks

## Task 1: Iterate and Inspect
Loop through the input list.

## Task 2: Validate and Convert
- If item is `int`: use it.
- If item is `str`: `try` to convert to `int`. Catch `ValueError` to ignore bad strings.
- If item is `None` or other types: ignore.

## Task 3: Calculate Average
Sum of valid items / Count of valid items.
- Edge case: If valid items count is 0, return 0.0.
