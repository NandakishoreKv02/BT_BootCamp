# Unit 1.8: Functions - Learning Outcomes

## Overview
Functions are the basic building blocks of modular programs. They allow you to group related code into reusable named blocks, making your programs easier to read, test, and maintain. In healthcare, functions process vitals, calculate dosages, and validate patient records consistently across an entire hospital system.

**Estimated Time**: 14-16 hours
- Knowledge: 2 hours
- Exercises: 4-6 hours
- App Labs: 8 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Function Fundamentals
- [ ] **Define** functions using the `def` keyword with appropriate naming conventions.
- [ ] **Call** functions and understand the flow of execution.
- [ ] **Implement** return values to send data back to the caller.

### Parameters & Arguments
- [ ] **Differentiate** between positional and keyword arguments.
- [ ] **Implement** default parameter values to handle common scenarios (e.g., a default units parameter for weights).
- [ ] **Use** multiple parameters to build flexible, high-utility functions.

### Scope & Documentation
- [ ] **Trace** variable scope to distinguish between local and global variables.
- [ ] **Explain** the risks of overusing global variables in critical systems.
- [ ] **Write** professional Docstrings (PEP 257) to document purpose, parameters, and return types.

### Design Principles
- [ ] **Follow** the "Single Responsibility Principle" (one function, one task).
- [ ] **Identify** and refactor repetitive code into reusable functions.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct definition of functions with multiple parameters.
- Effective use of default arguments to simplify function calls.
- Proper variable scope management (no unintentional global modifications).
- Detailed Docstring implementation for all functions.

### App Labs (Pass: 80% or higher)
- **Modularity**: Breaking down a complex medical calculation into smaller, helper functions.
- **Robustness**: Handling missing or invalid inputs using default values or return logic.
- **Maintainability**: Using clear, descriptive function names and parameter labels.
- **Documentation**: Providing clear docstrings that explain units (e.g., "mg", "kg", "lbs").

---

## Next Steps
1. **Module 1.9: Lambda Functions** will introduce anonymous, one-line functions.
2. **Module 3: Modular Programming** will teach you how to organize these functions into separate files (modules).

---

## Common Pitfalls to Avoid
✅ **Do**: Give functions names that start with a verb (e.g., `calculate_bmi()`, `verify_access()`).

❌ **Don't**: Use vague names like `func1()` or `process_data()`.

✅ **Do**: Keep functions small and focused on one specific task.

❌ **Don't**: Write "Monster Functions" that are 100+ lines long and do 5 different things.

✅ **Do**: Use keyword arguments when calling functions with many parameters to improve clarity.

❌ **Don't**: Rely purely on position if it's not obvious what each number represents (e.g., `calc(10, 5, 2, True)`).

✅ **Do**: Avoid using the `global` keyword inside functions; pass data in via arguments and out via returns instead.

❌ **Don't**: Modify global application state from deep inside a utility function.

✅ **Do**: Use `return` once per logical path in a function.

❌ **Don't**: Forget that a function with no `return` statement implicitly returns `None`.
