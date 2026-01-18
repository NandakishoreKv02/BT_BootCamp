# Lab 1 Tasks

## Task 1: The Runner
- Implement `execute_transaction(db, func)`.
- Set `db.is_locked = True`.
- In `try`, execute `func()`.
- In `finally`, set `db.is_locked = False`.

## Task 2: Verification
- Verify that if `func()` succeeds, lock is released.
- Verify that if `func()` raises `ValueError`, lock is released (AND the exception still bubbles up).

## Task 3: Error Handling
- Note: The `execute_transaction` function should NOT catch the exception. It should let it propagate. It's only responsible for cleanup.
