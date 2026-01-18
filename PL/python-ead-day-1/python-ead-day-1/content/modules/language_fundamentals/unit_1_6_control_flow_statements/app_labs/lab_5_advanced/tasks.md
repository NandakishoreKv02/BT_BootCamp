# Lab 5: Hospital Queue Manager - Tasks

## Task 1: Setup
Create `admitted_names` (list) and `routine_count` (int) variables.

## Task 2: Core Loop
Iterate through the `queue` using a `for` loop.

## Task 3: Hard Limit
Calculate the `absolute_limit` as `capacity * 2`. 
If the current number of admitted patients equals this limit, `break`.

## Task 4: Conditional Admission
- If patient is `urgent`:
  Add them to `admitted_names`.
- Else (if not urgent):
  Only add them to `admitted_names` AND increment `routine_count` if `routine_count` is less than `capacity`.
