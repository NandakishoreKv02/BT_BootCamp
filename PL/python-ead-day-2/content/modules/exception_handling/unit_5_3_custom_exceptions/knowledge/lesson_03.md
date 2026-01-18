---
title: Custom Exceptions
type: knowledge
module: exception_handling
unit: unit_5_3_custom_exceptions
order: 3
difficulty: intermediate
tags:
  subtopics:
    - inheritance
    - custom-attributes
    - exception-hierarchy
    - design-patterns
---

# Unit 5.3: Custom Exceptions

## 1. What

**Custom Exceptions** are user-defined classes that inherit from Python's built-in `Exception` class. They allow you to represent errors specific to your application's domain (e.g., `InsufficientFundsError`, `PatientDischargedError`) rather than reusing generic Python errors like `ValueError`.

### Core Concepts
| Concept | Description |
|---------|-------------|
| **Inheritance** | All custom exceptions must inherit from `Exception` (or a subclass of it). |
| **Naming** | Convention dictates ending the class name with `Error` (e.g., `ValidationError`). |
| **Attributes** | You can store extra data (e.g., `user_id`, `timestamp`) in the exception instance. |
| **Hierarchy** | Grouping errors under a common base class allows catching groups of errors easily. |

---

## 2. Example

### Example 1: Basic Custom Exception
```python
class InsufficientStockError(Exception):
    """Raised when requesting more items than available."""
    pass

def withdraw_stock(current, quantity):
    if quantity > current:
        raise InsufficientStockError(f"Cannot withdraw {quantity}, only {current} left.")
    return current - quantity
```

### Example 2: Adding Attributes
```python
class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

try:
    raise APIError("Not Found", 404)
except APIError as e:
    print(f"Error {e.status_code}: {e}")
```

### Example 3: Hierarchy
```python
class MyAppError(Exception): pass
class DatabaseError(MyAppError): pass
class NetworkError(MyAppError): pass

try:
    # Some logic
    pass
except MyAppError:
    # Catches BOTH DatabaseError and NetworkError, but NOT ValueError/KeyError
    print("An application-specific error occurred.")
```

---

## 3. Explanation

### Why Inheritance Matters
Python's `try-except` block works by checking `isinstance(raised_error, caught_class)`.
- If `DatabaseError` inherits from `MyAppError`, then `except MyAppError` catches it.
- Never inherit from `BaseException` directly unless you are building a system-level framework (like a task runner handling generic exits).

### Naming Conventions
Follow PEP 8: `CamelCase` names ending in `Error`.
- `InvalidInputError` (Good)
- `InputInvalid` (Bad - unclear it's an exception)
- `MyException` (Vague)

### Adding Attributes
The `super().__init__(message)` call is important. It ensures the standard string representation (`str(e)`) works as expected. You can extend `__init__` to accept and store whatever other context is useful for debugging or recovery logic.

---

## 4. Why

### 1. Expressiveness
`raise ValueError("User not found")` vs `raise UserNotFoundError(user_id)`. The second is self-documenting and carries semantic meaning.

### 2. Precise Control Flow
If you use `ValueError` for everything, you have to parse the error string to distinguish between "Invalid Age" vs "Invalid Name". With custom classes, you just use different `except` blocks.

### 3. API Design
Libraries often report errors specific to their domain. `requests` raises `requests.exceptions.ConnectionError`, not `socket.error`, shielding the user from implementation details.

---

## 5. Advantages & Disadvantages

### Advantages
| Advantage | Description |
|-----------|-------------|
| Granular Catching | Catch specific logic failures without catching simple bugs (like helper function `ValueError`s). |
| Data Payload | Pass structured data (codes, IDs) up the stack. |
| Grouping | Catch all app errors with one handler via a base class. |

### Disadvantages
| Disadvantage | Description |
|--------------|-------------|
| Verbosity | Requires defining more classes. |
| Maintenance | You have to maintain legacy exception names if you change your mind later (backward compatibility). |

---

## 6. Real-World Use Cases

### Healthcare: Validation Hierarchy
**Problem**: An insurance claim can be rejected for many reasons: 'Policy Expired', 'Duplicate Claim', 'Invalid Code'.
**Solution**:
- Base: `ClaimRejectionError`
- Children: `PolicyExpiredError`, `DuplicateClaimError`
- Code: `except ClaimRejectionError` handles the general "rejection" flow (notify user), while specific handlers can trigger specific fix workflows (e.g., auto-archive duplicates).

### Healthcare: Smart Alerts
**Problem**: A device fails. Is it critical?
**Solution**:
- `DeviceError(is_critical=True)`
- The centralized handler checks `if e.is_critical: page_doctor()`.

---

## 7. Best Practices

### Best Practice 1: Define a Base Class
Always define `class ModuleError(Exception): pass` for your project. Make all other custom exceptions inherit from it. This allows users of your module to catch `ModuleError` to catch *anything* your module throws.

### Best Practice 2: Keep It Simple
Most custom exceptions don't need logic. `class MyError(Exception): pass` is usually sufficient. Only add `__init__` override if you need to enforce structured arguments.

### Best Practice 3: Don't Shadow Built-ins
Don't name your exception `ValueError` or `TypeError`. It will confuse readers and potentially shadow the built-ins if imported improperly.

---

## 8. Top 3 Mistakes

### Mistake 1: Inheriting from `BaseException`
`except Exception:` will NOT catch your error. This is usually not what you want for an application error.

### Mistake 2: Overusing Custom Exceptions
Creating a new class for every single error message (e.g., `UserEmailInvalidError`, `UserNameRunningError`). Sometimes `ValidationError("Email invalid")` is enough. Balance granularity with sanity.

### Mistake 3: Breaking the `str(e)` Contract
If you override `__init__` but forget to call `super()`, or don't set a message, printing the exception might show nothing, making logs useless.
