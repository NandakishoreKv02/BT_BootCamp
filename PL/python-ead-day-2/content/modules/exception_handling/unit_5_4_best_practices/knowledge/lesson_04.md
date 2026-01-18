---
title: Exception Handling Best Practices
type: knowledge
module: exception_handling
unit: unit_5_4_best_practices
order: 4
difficulty: intermediate
tags:
  subtopics:
    - eafp-vs-lbyl
    - specific-exceptions
    - logging
    - performance
    - user-ux
---

# Unit 5.4: Exception Handling Best Practices

## 1. What

This unit focuses on the "Should" and "How" of exception handling. Beyond the syntax, we look at the standards that separate senior Python developers from beginners. We cover the Pythonic philosophy of **EAFP**, the necessity of **Specific Handling**, and the mechanics of **Production Logging**.

### Core Philosophies
| Philosophy | Acronym | Description |
|------------|---------|-------------|
| **Easier to Ask for Forgiveness than Permission** | **EAFP** | Assume everything works, catch errors if they don't. (Pythonic). |
| **Look Before You Leap** | **LBYL** | Check all conditions before performing a task. (C/Java style). |

---

## 2. Example

### Example 1: EAFP (The Pythonic Way)
```python
# EAFP approach
def process_record(data):
    try:
        age = data["age"]
        print(f"Age is {age}")
    except KeyError:
        print("Age missing.")
```

### Example 2: LBYL (The "Un-Pythonic" Way)
```python
# LBYL approach
def process_record(data):
    if "age" in data:
        age = data["age"]
        print(f"Age is {age}")
    else:
        print("Age missing.")
```

### Example 3: Proper Logging
```python
import logging

try:
    1 / 0
except ZeroDivisionError:
    # Includes the full traceback automatically
    logging.exception("Math fail in calculator module") 
```

---

## 3. Explanation

### EAFP vs LBYL
In Python, EAFP is generally preferred because:
1.  **Race Conditions**: In LBYL, `if os.path.exists(file): open(file)` can fail if another process deletes the file *between* the check and the open. EAFP handles it atomically by just trying the open.
2.  **Readability**: The "Happy Path" is cleaner. You don't have deeply nested `if` statements checking every possible failure before doing work.

### Specific vs General Exception Handling
Never do this:
```python
try:
    process()
except:  # WRONG: Catches everything, including Ctrl+C
    pass
```
Always do this:
```python
try:
    process()
except (ValueError, KeyError) as e: # Catch what you expect
    handle(e)
```
Catching `Exception` should be reserved for the outermost layer of your application (the "Top Level") to log unexpected crashes before the program terminates.

### Logging Exceptions
Use the `logging` module. Never use `print()` for errors in a professional application.
- `logging.error(e)`: Logs just the message.
- `logging.exception("msg")`: Logs the message PLUS the full stack trace. This is gold for debugging.

---

## 4. Why

### 1. Robustness
LBYL checks can be incomplete. You might check if a file exists, but forget to check if you have permission to read it. EAFP catches the `OSError` regardless of the specific cause.

### 2. Security
Showing a patient a "Database Error at /usr/local/lib/..." is a security risk. It tells a hacker your file structure. Best practice is to log the technical detail and show the user: "Our systems are experiencing a delay. Please try again later."

### 3. Maintainability
Code that uses specific exceptions communicates *intent*. If you catch `KeyError`, the next developer knows exactly what you were worried about.

---

## 5. Advantages & Disadvantages

### Advantages
| Advantage | Description |
|-----------|-------------|
| Atomic Operations | EAFP prevents "Check-then-Action" race conditions. |
| Clean Happy Path | Business logic isn't cluttered with `if` checks. |
| Traceability | Proper logging creates a searchable history of failures. |

### Disadvantages
| Disadvantage | Description |
|--------------|-------------|
| Performance | Creating an exception object is slower than a simple `if` check. (Only matters in tight loops). |
| Over-Catching | If your `try` block is too big, you might catch a `KeyError` you didn't expect from a completely different line. |

---

## 6. Real-World Use Cases

### Healthcare: Patient ID Mapping
**Problem**: Mapping a local facility ID to a national ID.
**Solution**: Use EAFP with a dictionary. If the ID doesn't exist, the `KeyError` handler triggers a new registration workflow.

### Healthcare: Vital Signs Stream
**Performance Note**: If you are receiving 1,000 heart rate packets per second, avoid using exceptions for "Missing Heartbeat". Use LBYL (`if packet.hb is None`) because the overhead of 1,000 exceptions per second will spike the CPU.

---

## 7. Best Practices

### Best Practice 1: Narrow Scope
Keep the `try` block as small as 1-3 lines. Specifically, only wrap the code that is *intended* to fail.

### Best Practice 2: Contextual Logging
Always log metadata. `logging.error(f"Failed to find record for patient {pid}")` is better than `logging.error("Not found")`.

### Best Practice 3: Handle or Raise
If you catch an exception but don't know how to fix it, log it and **RE-RAISE** it. Never swallow exceptions unless you are 100% sure the program can continue safely.

---

## 8. Top 3 Mistakes

### Mistake 1: The Bare Except
`except:` catches `SystemExit`, making it impossible to stop your script with `Ctrl+C`. Use `except Exception:` if you must catch all program errors.

### Mistake 2: Swallowing Silent Failures
```python
except Exception:
    pass
```
**Impact**: Bugs stay hidden for weeks, and you'll never know why some data is missing.

### Mistake 3: User Facing Technicalities
Displaying raw tracebacks to a GUI user.
**Impact**: Bad user experience and security leak.
