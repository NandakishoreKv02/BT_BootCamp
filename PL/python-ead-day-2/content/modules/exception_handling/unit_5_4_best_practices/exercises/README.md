# Unit 5.4: Exception Handling Best Practices - Exercises

## Overview

This unit contains 8 progressive drills focusing on applying Pythonic standards to error management.

**File**: `unit_5_4_best_practices_exercises.py`

---

## Exercise List

### Exercise 1: LBYL to EAFP (Dict)
**Objective**: Refactor look-ahead code to a more Pythonic style.

**Description**: You have an LBYL function that checks if a key exists in a dict before accessing. Refactor it to use EAFP (`try-except KeyError`).

---

### Exercise 2: LBYL to EAFP (Division)
**Objective**: Avoid double-checking values.

**Description**: Refactor a function that checks `if b != 0` to use EAFP (`try-except ZeroDivisionError`).

---

### Exercise 3: Specificity Check
**Objective**: Avoid the "Bare Catch" anti-pattern.

**Description**: You are given code that catches the generic `Exception`. Fix it to catch only the specific errors that can occur (e.g., `AttributeError`).

---

### Exercise 4: Clean Happy Path
**Objective**: Minimize the size of the `try` block.

**Description**: A function has 10 lines of code inside a `try` block. Only the second line can actually fail. Refactor the code so only that line is wrapped.

---

### Exercise 5: Basic Exception Logging
**Objective**: Use the `logging` module.

**Description**: Implement `log_error(func)`. Use `logging.error` to catch a generic exception and log the message string.

---

### Exercise 6: Advanced Logging (Traceback)
**Objective**: Capture the stack trace.

**Description**: Implement `log_full_crash(func)`. Use `logging.exception()` to catch an error. This should automatically record the traceback.

---

### Exercise 7: User-Friendly Messages
**Objective**: Separate internal logs from user display.

**Description**: Create a function that handles a `PermissionError`. It should log the technical detail (including path) to a list, but return a simple string for the user: "Access Denied. Please contact your administrator."

---

### Exercise 8: Performance Loop (LBYL Preferred)
**Objective**: Identify cases where LBYL is better.

**Description**: In a loop of 1,000,000 iterations, most values will be `None`. Write an LBYL check (`if x is not None`) and explain why it's better here than EAFP (Performance).

**Hints**:
- "Pythonic" usually means EAFP.
- `logging.exception()` must be called inside an `except` block.
- Keep the `try` block scope as narrow as possible.
