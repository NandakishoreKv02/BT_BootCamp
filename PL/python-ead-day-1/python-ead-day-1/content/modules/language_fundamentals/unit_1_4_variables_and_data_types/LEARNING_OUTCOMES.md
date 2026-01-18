# Unit 1.4: Variables & Data Types - Learning Outcomes

## Overview
In this unit, you will dive deep into Python's type system. You'll learn how to effectively use variables, adhere to professional naming conventions (PEP 8), and master the primitive data types that form the building blocks of all Python programs. You will also explore type checking, type casting, and the fundamental concept of mutability versus immutability.

**Estimated Time**: 8-10 hours
- Knowledge: 90 min
- Exercises: 3 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Variables and Dynamic Typing
- [ ] **Define** variables and understand Python's dynamic typing nature (variables are references to objects).
- [ ] **Manage** memory efficiently by understanding how Python handles variable assignment and reference counting.
- [ ] **Apply** correct variable naming conventions (snake_case) following PEP 8 guidelines.

### Primitive Data Types
- [ ] **Utilize** `int` and `float` for numerical calculations in healthcare scenarios (e.g., dosage, BMI).
- [ ] **Manipulate** text data using the `str` type, including escaping characters and multi-line strings.
- [ ] **Implement** logic using the `bool` type (True/False) for control flow.

### Type Checking & Inspection
- [ ] **Inspect** variable types at runtime using `type()`.
- [ ] **Validate** types using `isinstance()` for robust error handling.
- [ ] **Explain** why `isinstance()` is preferred over `type()` (inheritance support).

### Type Casting & Conversions
- [ ] **Convert** between types explicitly (e.g., `str` to `int`, `float` to `int`).
- [ ] **Handle** value errors during conversion (e.g., converting "abc" to int).
- [ ] **Understand** implicit type conversion (coercion) during arithmetic operations.

### Mutability vs Immutability
- [ ] **Distinguish** between immutable types (int, float, bool, str, tuple) and mutable types (list, dict, set).
- [ ] **Predict** behavior when modifying variables of different types.
- [ ] **Explain** the performance and safety implications of immutability in multi-threaded applications.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of variable names following PEP 8.
- Successful implementation of type casting without crashing on invalid input.
- Accurate identification of variable types using `isinstance()`.
- Demonstration of string and number manipulation.

### App Labs (Pass: 80% or higher)
- **Data Integrity**: Correctly parsing and converting user input strings to appropriate numerical types.
- **Safety**: Handling type conversion errors gracefully.
- **Precision**: Using appropriate types for healthcare data (e.g., floats for temperature, ints for heart rate).
- **Style**: Consistent naming conventions (variables, functions, constants).

---

## Next Steps
1. **Unit 1.5: Operators & Expressions** will teach you how to perform operations on these data types.
2. **Unit 1.6: Control Flow** will use booleans and logic to control program execution.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `snake_case` for variable names (e.g., `patient_id`).

❌ **Don't**: Use `camelCase` or `PascalCase` for variables (reserved for classes).

✅ **Do**: Use `isinstance(val, int)` to check types.

❌ **Don't**: Use `type(val) == int` unless you specifically want to exclude subclasses.

✅ **Do**: Be careful with floating-point precision (e.g., `0.1 + 0.2 != 0.3`).

❌ **Don't**: Use floats for currency or precise medical dosages without rounding or `Decimal`.

✅ **Do**: Remember that strings are immutable—methods like `.upper()` return a *new* string.

❌ **Don't**: Attempt to modify a string in place (e.g., `s[0] = 'A'` raises TypeError).

✅ **Do**: Handle exceptions when converting user input (e.g., `int("invalid")`).

❌ **Don't**: Assume all input strings are valid numbers.
