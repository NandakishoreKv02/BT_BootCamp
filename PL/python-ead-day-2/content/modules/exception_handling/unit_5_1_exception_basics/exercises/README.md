# Unit 5.1: Exception Basics - Exercises

## Overview

This unit contains 8 progressive drills focusing on Python's error handling mechanisms.

**File**: `unit_5_1_exception_basics_exercises.py`

---

## Exercise List

### Exercise 1: Basic Try-Except
**Objective**: Handle a division-by-zero error.

**Description**: Create a function `safe_divide(a, b)` that returns the result of `a / b`. If `b` is zero, catch the `ZeroDivisionError` and return `None`.

---

### Exercise 2: Catching Multiple Exceptions
**Objective**: Handle multiple types of errors in a conversion function.

**Description**: Implement `parse_age(age_string)`. It should convert the string to an integer. Handle `ValueError` (invalid string) and `TypeError` (if input is None) by returning `-1`.

---

### Exercise 3: Accessing Exception Details
**Objective**: Extract the error message from the exception object.

**Description**: Write a function `get_key(data, key)` that retrieves a value from a dictionary. If the key is missing, catch the `KeyError` as `e` and return the string version of the error message (e.g., `'missing_key'`).

---

### Exercise 4: The Else Clause
**Objective**: Execute code only on success.

**Description**: Create a function `validate_and_process(data)`. In a try block, convert data to a list. If it raises `TypeError`, return `"Invalid Type"`. In the `else` block (only if conversion worked), return the length of the list.

---

### Exercise 5: Exception Hierarchy (LookupError)
**Objective**: Use a parent exception to catch multiple child errors.

**Description**: Create `safe_lookup(container, index_or_key)`. Try to access the container. Catch `LookupError` (which covers both `IndexError` and `KeyError`) and return `"Not Found"`.

---

### Exercise 6: Catching bare Exception (Anti-pattern awareness)
**Objective**: Demonstrate how `except Exception` catches unforeseen errors.

**Description**: Write `catch_all(func)`. Execute the passed function `func`. Catch `Exception` (catch-all non-system errors) and return `"Caught Error"`. If no error, return `"Success"`.

---

### Exercise 7: Nested Try-Except
**Objective**: Handle errors at different levels.

**Description**: implement `complex_process(dict_list, index, key)`. Outer try: access list by index (handle `IndexError` -> return "Bad Index"). Inner try: access dict by key (handle `KeyError` -> return "Bad Key").

---

### Exercise 8: Handling Attribute Errors
**Objective**: Safely access object properties.

**Description**: Create `get_status(obj)`. Try to return `obj.status`. Catch `AttributeError` if the property doesn't exist and return `"Unknown Status"`.

**Hints**:
- Remember that `else` runs only if `try` succeeds.
- `LookupError` is the parent of `KeyError` and `IndexError`.
- Use `str(e)` to convert an exception object to its message string.
