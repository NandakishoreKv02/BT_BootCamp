---
title: Advanced Exception Handling
type: knowledge
module: exception_handling
unit: unit_5_2_advanced_exception_handling
order: 2
difficulty: intermediate
tags:
  subtopics:
    - finally-clause
    - nested-try-except
    - exception-chaining
    - re-raising
    - context-managers
---

# Unit 5.2: Advanced Exception Handling

## 1. What

This unit covers advanced patterns for ensuring system stability and debuggability. While `try-except` handles the error, `finally` and `with` handle the **cleanup** (Resource Management). Additionally, exception chaining allowing you to "translate" cryptic system errors into meaningful application errors without losing the original context.

### Core Concepts
| Concept | Keyword/Syntax | Description |
|---------|----------------|-------------|
| **Finally** | `finally:` | Executes code regardless of success or failure. Used for cleanup. |
| **Re-raising** | `raise` | Catches an error to perform an action (e.g., log) and then lets it bubble up. |
| **Chaining** | `raise NewErr from OldErr` | Wraps an original low-level error in a high-level error. |
| **Context Manager** | `with ... as ...` | Automates parsing of setup/teardown logic (like opening/closing files). |

---

## 2. Example

### Example 1: The Finally Block
```python
file = None
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File missing.")
finally:
    # This runs whether try failed, succeeded, or even returned early!
    if file:
        file.close()
        print("File closed.")
```

### Example 2: Exception Chaining
```python
def connect_to_database():
    try:
        _low_level_connect()
    except TimeoutError as e:
        # Wrap the technical error in a domain error
        raise ConnectionError("Database is offline") from e

# Traceback will show:
# The above exception (TimeoutError) was the direct cause of the following exception:
# ConnectionError: Database is offline
```

### Example 3: Context Managers (The Pythonic Way)
Replacing `try-finally` for resources:
```python
try:
    with open("data.txt", "r") as f:
        data = f.read()
    # f.close() is called automatically here
except FileNotFoundError:
    print("File missing")
```

---

## 3. Explanation

### The `finally` Clause
The `finally` block is the "guarantee" block. It executes no matter what happens in the `try` block:
- If try finishes normally: `finally` runs.
- If try raises an exception: `finally` runs, *then* the exception continues (unless caught).
- If try executes `return`: `finally` runs *before* the function actually returns.

### Nested Try-Except
You can put `try` blocks inside `except` blocks.
```python
try:
    process()
except ConnectionError:
    try:
        reconnect()  # Nested try to handle recovery failure
    except ConnectionError:
        print("Recovery failed too.")
```

### Re-raising Exceptions
Sometimes you want to observe an error but not stop it.
```python
try:
    process_payment()
except PaymentFailed:
    logging.error("Payment failed user_id=123")
    raise  # Re-raises the exact same PaymentFailed exception
```

### Exception Chaining (`raise from`)
When building libraries or large apps, low-level errors (like `KeyError` in a config parser) are confusing to end users. Chaining allows you to catch the `KeyError` and raise a `ConfigurationError`, while attaching the original `KeyError` as the `__cause__`. This creates a beautiful "linked list" of errors in the traceback.

### Context Managers (`with`)
The `with` statement simplifies resource management. Any object that defines `__enter__` and `__exit__` methods is a context manager. It replaces the boilerplate of `try...finally`. Common uses: files, network connections, thread locks, database transactions.

---

## 4. Why

### 1. Resource Leaks
Without `finally` or `with`, an error occurring before `file.close()` leaves the file handle open. In a server processing thousands of requests, this leads to "Too many open files" crashes.

### 2. Better Debugging
Chaining (`raise from`) tells the story of *why* an error occurred. Instead of just seeing "KeyError: 'port'", you see "DatabaseConnectionError: Failed to connect" caused by "KeyError: 'port'".

### 3. Transactional Integrity
If a multi-step operation fails halfway, `finally` blocks can be used to roll back changes, ensuring the system isn't left in a broken state.

---

## 5. Advantages & Disadvantages

### Advantages
| Advantage | Description |
|-----------|-------------|
| Guaranteed Cleanup | `finally` ensures locks/files/connections are released. |
| Context Preservation | Chaining keeps the original error trace alive. |
| Readability | `with` statements reduce boilerplate code significantly. |

### Disadvantages
| Disadvantage | Description |
|--------------|-------------|
| Complexity | Nested try-excepts can become "arrow code" (hard to read). |
| Return Confusion | A `return` inside `finally` swallows any active exception from the `try` block! (Anti-pattern). |

---

## 6. Real-World Use Cases

### Healthcare: Medical Record Lock
**Problem**: Two doctors trying to edit a record. You use a `Lock`.
**Solution**: Use `try...finally` (or `with lock:`) to ensure the lock is released even if the update crashes. Otherwise, the record remains locked forever.

### Healthcare: Critical Alert System
**Problem**: Sending an alert to a pager API.
**Solution**: If the basic HTTP request fails (`ConnectionError`), catch it and raise a `CriticalAlertFailure` exception chained from the original error, so the on-call engineer knows both *that* alerting failed and *why* (network vs auth).

---

## 7. Best Practices

### Best Practice 1: Prefer `with` over `finally`
If a standard context manager exists (like for files or locks), use it. It's cleaner and less error-prone.

### Best Practice 2: Always Chain Wrapped Exceptions
If you catch an exception and raise a new one, ALWAYS use `raise NewError from e`. Never just `raise NewError`, or you lose the original stack trace.

### Best Practice 3: Keep `finally` Simple
Put complex logic in `finally`. If `finally` itself raises an exception, the original exception (if any) is lost (swallowed).

---

## 8. Top 3 Mistakes

### Mistake 1: Swallowing Exceptions in `except`
```python
except ValueError:
    print("Oops")
    # No raise? The program continues as if nothing happened!
```
**Impact**: The calling function thinks success occurred, potentially iterating over `None` data later.

### Mistake 2: Returning in `finally`
```python
try:
    raise ValueError()
finally:
    return True  # This SWALLOWS the ValueError!
```
**Impact**: The caller receives `True` instead of seeing the error.

### Mistake 3: Bare Re-raise (`raise e`)
```python
except ValueError as e:
    raise e  # Bad. Modifies the stack trace to start here.
    # raise  # Good. Preserves the stack trace.
```
**Impact**: Makes debugging harder because the traceback points to the `except` block, not the original error line.
