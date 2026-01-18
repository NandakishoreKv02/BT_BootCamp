# Unit 5.2: Advanced Exception Handling - Exercises

## Overview

This unit contains 8 progressive drills focusing on comprehensive error management strategies.

**File**: `unit_5_2_advanced_exception_handling_exercises.py`

---

## Exercise List

### Exercise 1: The Finally Block
**Objective**: Ensure cleanup occurs.

**Description**: Create a function `process_and_clean(data)`. In `try`, verify data is a list (raise `TypeError` if not). Ensure that regardless of success or error, a global "cleanup_done" flag is set to True in `finally`.

---

### Exercise 2: Re-raising Exceptions
**Objective**: Log (print) an error locally and then propagate it.

**Description**: Implement `log_and_rethrow(func)`. Run `func()`. If it raises `ValueError`, print "Logging Error", then **re-raise** the same exception so the caller sees it.

---

### Exercise 3: Exception Chaining
**Objective**: Convert low-level errors to domain errors.

**Description**: Implement `connect_db()`. Simulate a `TimeoutError`. Catch it and raise a `RuntimeError` with the message "DB Connection Failed" using the `raise ... from` syntax.

---

### Exercise 4: Nested Try-Except
**Objective**: Handle a primary failure with a fallback that can also fail.

**Description**: Implement `redundant_fetch()`. Outer try: call `fetch_primary()`. If it fails (`ValueError`), inner try: call `fetch_backup()`. If backup also fails (`ValueError`), return "All Failed". If primary succeeds, return "Primary". If backup succeeds, return "Backup".

---

### Exercise 5: Context Manager (File)
**Objective**: Use `with` for file handling.

**Description**: Create `read_file_safe(path)`. Use `with open(...)` to read the file. Catch `FileNotFoundError` and return `None`. This ensures the file is closed automatically.

---

### Exercise 6: Inspecting Exception Objects
**Objective**: Access arguments of an exception.

**Description**: Create `get_error_code(func)`. Run `func()`. Catch `ValueError`. Return the first argument stored in the exception instance (e.g., `e.args[0]`). If no error, return `None`.

---

### Exercise 7: Try-Except-Else-Finally
**Objective**: Combine all blocks.

**Description**: Implement `full_flow(val)`.
- Try: `10 / val`.
- Except `ZeroDivisionError`: return "Error".
- Else: return "Success".
- Finally: append "Done" to a global list (provided as arg).

---

### Exercise 8: Catching Custom Errors
**Objective**: Define and catch a custom exception.

**Description**: Define `class MyError(Exception): pass`. Write a function `trigger_and_catch()` that raises `MyError` and catches it, returning "Caught Custom".

**Hints**:
- `raise` without arguments re-raises the active exception.
- `raise New from Old` sets the `__cause__` attribute.
- `finally` always runs.
