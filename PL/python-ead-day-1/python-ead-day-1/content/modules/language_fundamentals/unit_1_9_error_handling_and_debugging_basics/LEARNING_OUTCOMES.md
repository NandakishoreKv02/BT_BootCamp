# Unit 1.9: Error Handling & Debugging Basics - Learning Outcomes

## Overview
Programming errors are inevitable. In critical healthcare systems—where a crashed program could delay patient care—graceful error handling is a mandatory skill. This unit covers how to categorize errors, handle predictable exceptions, and systematically find and fix bugs using standard debugging techniques.

**Estimated Time**: 12-14 hours
- Knowledge: 2 hours
- Exercises: 4 hours
- App Labs: 6-8 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Error Categorization
- [ ] **Distinguish** between Syntax Errors (compile-time) and Exceptions (runtime).
- [ ] **Identify** common built-in exceptions: `ValueError`, `TypeError`, `KeyError`, `IndexError`, and `ZeroDivisionError`.

### Exception Handling
- [ ] **Implement** `try...except` blocks to prevent program crashes during data processing.
- [ ] **Utilize** `else` and `finally` blocks for clean-up operations (e.g., closing a connection).
- [ ] **Catch** specific exceptions to provide meaningful feedback to the user or system log.

### Debugging Basics
- [ ] **Apply** print-based debugging to trace the flow of values and logic.
- [ ] **Read** and interpret Python tracebacks to locate the line and cause of an error.
- [ ] **Adopt** a systematic debugging mindset: Reproduce, Isolate, Fix, and Verify.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct usage of `try/except` to handle division by zero.
- Successful handling of missing keys in a dictionary without crashing.
- Proper conversion of "dirty" string data to numbers using error trapping.

### App Labs (Pass: 80% or higher)
- **Stability**: The application should never crash, even when given "garbage" input (e.g., text instead of vitals).
- **Feedback**: Providing clear error messages instead of raw tracebacks.
- **Cleanup**: Using `finally` to ensure program state is consistent after an error.
- **Traceability**: Using strategic `print()` calls during development to solve intermediate logical bugs.

---

## Next Steps
1. **Module 1.10: Final Project** will require you to combine functions, data structures, and error handling into a complete Clinical Dashboard.

---

## Common Pitfalls to Avoid
✅ **Do**: Catch specific exceptions (e.g., `except ValueError:`) to know exactly what went wrong.

❌ **Don't**: Use a "bare" `except:` block unless absolutely necessary; it can hide serious bugs.

✅ **Do**: Use `finally` for code that must run regardless of success or failure (like logging an exit).

❌ **Don't**: Use exceptions for normal program logic (e.g., checking if a list is empty). Use `if` statements for logic and `try/except` for true unexpected errors.

✅ **Do**: Read the *last line* of a traceback first—it tells you the error name and message.

❌ **Don't**: Ignore the line number provided in the traceback.
