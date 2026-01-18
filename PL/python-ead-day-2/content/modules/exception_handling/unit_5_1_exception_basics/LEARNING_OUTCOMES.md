# Unit 5.1: Exception Basics - Learning Outcomes

## Overview
Learn the fundamental mechanisms of error handling in Python. This unit covers how to gracefully handle runtime errors, prevent application crashes, and control program flow when unexpected situations occur—critical for reliable medical record processing and patient data systems.

**Estimated Time**: 4-6 hours
- Knowledge: 45 min
- Exercises: 60-90 min
- App Labs: 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Core Concepts
- [ ] **Identify** common built-in exceptions (`ValueError`, `TypeError`, `KeyError`, `IndexError`) and when they occur.
- [ ] **Understand** the Python exception hierarchy and inheritance structure.

### Practical Implementation
- [ ] **Implement** `try-except` blocks to catch and handle runtime errors gracefully.
- [ ] **Handle** multiple exception types using single or multiple `except` blocks.
- [ ] **Use** the `else` clause to execute code only when no exceptions occur.
- [ ] **Access** exception objects to log or analyze error details.

### Real-World Application (Healthcare)
- [ ] **Validate** patient input data without crashing the application.
- [ ] **Process** varied medical record formats robustly.
- [ ] **Implement** safe data lookup mechanisms for hospital inventories.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct usage of `try`, `except`, and `else` keywords.
- Accurate catching of specific exception types (avoiding bare `except:`).
- Proper access to error messages via the exception instance.

### App Labs (Pass: 80% or higher)
- **Robustness**: Applications must not crash when given invalid input (e.g., negative ages, missing keys).
- **Clarity**: Error messages returned to the user should be informative, not raw Python tracebacks.
- **Precision**: Catching the correct specific error rather than a generic `Exception`.

---

## Next Steps
1. **Move to Unit 5.2: Resource Management** to learn about `finally` and context managers.
2. **Review** the built-in exception hierarchy in the Python documentation.

---

## Common Pitfalls to Avoid
✅ **Do**: Catch specific exceptions like `ValueError` or `KeyError` whenever possible.
❌ **Don't**: Use a bare `except:` clause (catching *everything*) unless you absolutely intend to suppress all errors, including system exits.

✅ **Do**: Use the `else` block for code that should run only if the `try` block succeeds.
❌ **Don't**: Put every single line of code inside the `try` block; keep it focused on the potentially error-prone operation.

---

## Self-Assessment Questions
1. What is the difference between `except Exception as e:` and `except:`?
2. Why is `ZeroDivisionError` separate from `ValueError`?
3. When would you use an `else` block instead of simply putting the code after the `try-except`?
4. If a `KeyError` occurs inside a `try` block, and you have `except IndexError:`, will the program crash?
