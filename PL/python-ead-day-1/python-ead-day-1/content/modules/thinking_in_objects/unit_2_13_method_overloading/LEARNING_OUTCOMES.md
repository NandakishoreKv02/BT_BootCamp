# Unit 2.13: Method Overloading & Python's Approach - Learning Outcomes

## Overview
In many languages, "Overloading" means having multiple methods with the same name but different parameters. Python handles this differently. This unit explores how to use Python's dynamic nature—specifically default arguments and variable-length arguments—to achieve the same goal: creating flexible methods that can handle varying amounts and types of clinical data.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 2 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Explain Method Overloading** and how it functions in statically-typed languages.
- [ ] **Discuss why Python doesn't support traditional overloading**: Understand that the "last definition wins."
- [ ] **Identify the Default Argument Strategy**: How to simulate multiple signatures with a single method.
- [ ] **Distinguish between *args and **kwargs**: When to use positional vs. keyword variable arguments.
- [ ] **Identify when to avoid overloading**: Recognizing when separate method names are clearer for medical safety.

### Implementation Skills
- [ ] **Implement methods with Default Arguments** to handle optional medical parameters.
- [ ] **Use *args** to process a variable list of clinical metrics (e.g., multiple blood pressure readings).
- [ ] **Use **kwargs** to handle diverse metadata for patient records.
- [ ] **Perform type-checking inside a method** to provide different behaviors based on input types.

### Clinical System Design
- [ ] **Design a `DosageCalculator`** that accepts either a flat amount or a weight-based formula through the same method.
- [ ] **Build a `PatientSearch` utility** that works with just a name, or a name and a date of birth.
- [ ] **Develop a `LabAggregator`** that takes a variable number of separate test results.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of `*args` to sum dynamic clinical values.
- Successful implementation of a method using `**kwargs` for optional flags.
- Proper application of default arguments to simplify complex method signatures.

### App Labs (Pass: 80% or higher)
- **Flexibility**: The method can be called in at least three different ways (parameter counts/types).
- **Type Safety**: The method correctly identifies and handles different input types (e.g., int vs. list).
- **Code Cleanliness**: Avoiding deep if-else nests in favor of clean Pythonic argument handling.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Using Dispatchers or the `singledispatch` decorator for more advanced overloading-like behavior.

---

## Common Pitfalls to Avoid
✅ **Do**: Use default arguments (`param=None`) for 90% of "Overloading" needs.

❌ **Don't**: Define two methods with the same name. Only the second one will exist!

✅ **Do**: Use meaningful names for `*args` (e.g., `*vitals`) to improve readability.

❌ **Don't**: Use `*args` and `**kwargs` for everything. If a parameter is always required, name it explicitly for safety.
