# Lab 4 Tasks

## Task 1: Fetch Logic
- Implement `fetch_data(primary_func, backup_func)`.
- Try calling `primary_func()`. If success, return result.

## Task 2: First Fallback
- Catch `ValueError` (simulated failure).
- Inside the catch, try calling `backup_func()`. If success, return result.

## Task 3: Final Failure
- Catch `ValueError` from backup.
- Raise `RuntimeError("All sources failed")`.
