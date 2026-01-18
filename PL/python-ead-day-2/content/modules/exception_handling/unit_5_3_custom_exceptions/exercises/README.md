# Unit 5.3: Custom Exceptions - Exercises

## Overview

This unit contains 8 progressive drills focusing on defining and using custom exception classes.

**File**: `unit_5_3_custom_exceptions_exercises.py`

---

## Exercise List

### Exercise 1: Basic Definition
**Objective**: Define a simple custom exception.

**Description**: Define `class InvalidStateError(Exception)`. Write a function `check_state(state)` that raises this error if state is `"STOPPED"`.

---

### Exercise 2: Custom Message
**Objective**: Pass dynamic messages to custom exceptions.

**Description**: Define `class ValidationFailure(Exception)`. Write `validate_length(text, min_len)`. If `len(text) < min_len`, raise `ValidationFailure` with message "Text too short: X < Y".

---

### Exercise 3: Exception Attributes
**Objective**: Store extra data in the exception.

**Description**: Define `class HttpError(Exception)` that accepts `code` and `message` in `__init__`. Store `self.code`. Write `fake_fetch(url)` that raises `HttpError(404, "Not Found")` if url is "bad".

---

### Exercise 4: Inheritance Hierarchy
**Objective**: Create a tiered structure.

**Description**:
- Define `AppError(Exception)`.
- Define `AuthError(AppError)`.
- Define `PermissionError(AppError)`. (Note: this shadows built-in PermissionError, usually bad practice, but okay for exercise scope if scoped properly. Let's call it `AccessDeniedError` to be safe).
- Write `login(user)`. If user is "guest", raise `AuthError`. If user is "banned", raise `AccessDeniedError`.
- Caller should catch `AppError` to handle both.

---

### Exercise 5: Calling Super
**Objective**: Ensure proper initialization.

**Description**: Define `class DetailedError(Exception)`. `__init__` takes `msg` and `details`. It must call `super().__init__(msg)`. Store `details` attribute.

---

### Exercise 6: Catching Specifics
**Objective**: Distinguish between custom errors.

**Description**: Using the classes from Ex 4 (`AuthError`, `AccessDeniedError`), write a test harness `handle_login(user)` that catches `AuthError` -> returns "Auth Failed", catches `AccessDeniedError` -> returns "Access Denied", and `AppError` -> returns "Generic App Error".

---

### Exercise 7: Re-raising Custom
**Objective**: Wrap built-in error in custom error.

**Description**: Define `class ParseError(Exception)`. Write `safe_parse(text)`. Try `int(text)`. Except `ValueError`, raise `ParseError` from the original exception.

---

### Exercise 8: String Representation
**Objective**: Customize `__str__`.

**Description**: Define `class UserError(Exception)`. `__init__(user_id)`. Override `__str__` to return "Error for User [ID]". Raise and print it to verify.

**Hints**:
- Class definitions: `class Name(Parent): ...`
- `super().__init__(...)` is standard Python 3.
- `__str__` controls what `print(e)` shows.
