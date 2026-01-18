---
title: Exception Basics
type: knowledge
module: exception_handling
unit: unit_5_1_exception_basics
order: 1
difficulty: beginner
tags:
  subtopics:
    - try-except
    - built-in-exceptions
    - exception-hierarchy
    - else-clause
---

# Unit 5.1: Exception Basics

## 1. What

**Exception Handling** is a mechanism in Python used to handle runtime errors, allowing the normal flow of the program to be maintained. Instead of crashing when an error occurs (like dividing by zero or accessing a missing file), the program "catches" the error and executes alternative code.

### Core Keywords
| Keyword | Description |
|---------|-------------|
| **try** | The block of code to test for errors. |
| **except** | The block of code to execute if an error occurs. |
| **else** | The block of code to execute if NO error occurs. |
| **raise** | Used to manually trigger an exception (covered later). |

---

## 2. Example

### Example 1: Basic Error Handling

```python
def calculate_dose(mg, weight_kg):
    try:
        # Potentially risky operation
        dose = mg / weight_kg
    except ZeroDivisionError:
        # What to do if weight_kg is 0
        print("Error: Patient weight cannot be zero.")
        return None
    except TypeError:
        # What to do if inputs are not numbers
        print("Error: Inputs must be numbers.")
        return None
    else:
        # What to do if calculation succeeded
        print(f"Dose calculated successfully: {dose}")
        return dose

# Usage
calculate_dose(500, 0)      # Prints Error
calculate_dose(500, "70")   # Prints Error
calculate_dose(500, 70)     # Prints Success message
```

---

## 3. Explanation

### The Try-Except Block
The code inside the `try` block runs first. If an exception occurs:
1. Python stops the rest of the `try` block.
2. It looks for a matching `except` block.
3. If found, the code inside `except` runs.
4. If not found, the program crashes (propagates the error).

### Catching Multiple Exceptions
You can have multiple `except` blocks to handle different errors differently, or combine them:
```python
except (ValueError, TypeError):
    print("Invalid input format.")
```

### The Exception Hierarchy
All exceptions inherit from `BaseException`.
- `Exception` is the base class for all non-system-exiting exceptions.
- `ArithmeticError` contains `ZeroDivisionError`, `OverflowError`.
- `LookupError` contains `IndexError`, `KeyError`.

Understanding this hierarchy allows you to catch broader categories of errors. Catching `LookupError` will catch both missing dictionary keys AND invalid list indices.

### The Else Clause
The `else` block is optional. It runs **only if the try block raises NO exceptions**. It is useful for code that depends on the success of the `try` block but shouldn't be caught by the `except` handlers (avoiding accidental catching of bugs in the success logic).

---

## 4. Why

### 1. Robustness
In healthcare, software cannot simply crash. If one patient record is corrupt, the system must log the error and skip to the next patient, rather than halting the entire billing process.

### 2. User Experience
"IndexError at line 42" is useless to a doctor. "Patient ID not found" is helpful. Exception handling translates technical crashes into meaningful feedback.

### 3. Data Integrity
Proper handling ensures that half-finished operations don't leave databases in invalid states (though `finally`, covered next, is key here too).

---

## 5. Advantages & Disadvantages

### Advantages
| Advantage | Description |
|-----------|-------------|
| Prevents Crashes | Keeps the application running despite unexpected inputs. |
| Separation of Concerns | Separates "happy path" logic from error-handling logic. |
| Control Flow | Allows retry mechanisms or fallback values. |

### Disadvantages
| Disadvantage | Description |
|--------------|-------------|
| Performance | Trying and catching is slightly slower than direct validation (though negligible in most Python apps). |
| Masking Bugs | A bare `except:` can hide real bugs (like syntax errors or typos) making debugging a nightmare. |

---

## 6. Real-World Use Cases

### Healthcare: Patient Sensor Data
**Problem**: Reading data from a heart rate monitor stream. Sometimes the stream sends "N/A" or garbage text instead of a number.
**Solution**: Wrap the parsing logic in `try ... except ValueError` to ignore bad readings without stopping the monitoring loop.

### Healthcare: Drug Inventory Lookup
**Problem**: Looking up a drug price in a dictionary using a user-typed name.
**Solution**: Use `try ... except KeyError` to catch typos. Why not `if key in dict`? Pythonic style ("EAFP" - Easier to Ask Forgiveness than Permission) prefers try-except for its readability and atomic nature.

---

## 7. Best Practices

### Best Practice 1: Be Specific
Catch `ValueError` specifically, not just `Exception`. This ensures you don't accidentally catch a `KeyboardInterrupt` or a bug you didn't anticipate.

### Best Practice 2: Keep Try Blocks Small
Only wrap the line that might meaningfully fail.
**Bad**: Wrapping 50 lines of logic.
**Good**: Wrapping the single conversion or lookup line.

### Best Practice 3: Use Exception Instances
Capture the error message for logging:
```python
except ValueError as e:
    logging.error(f"Invalid value received: {e}")
```

---

## 8. Top 3 Mistakes

### Mistake 1: The Bare Except
```python
try:
    process_data()
except:
    pass 
```
**Impact**: This swallows EVERYTHING, including `Ctrl+C` (KeyboardInterrupt) and `SystemExit`. It makes it impossible to kill your script or debug typos.

### Mistake 2: Use Exception for Flow Control Logic
Using exceptions for standard business logic (e.g., using `ZeroDivisionError` to represent "Infinity" in a math library) can be confusing and slow. Use `if` statements for predictable conditions.

### Mistake 3: Catching Too Early
Catching an exception just to `print("Error")` and return `None` deeper in a library function might prevent the calling code from knowing something went wrong. Sometimes it's better to let the exception bubble up.
