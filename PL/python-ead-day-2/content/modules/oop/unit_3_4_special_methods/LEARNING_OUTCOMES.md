# Unit 3.4: Special Methods (Dunder Methods) - Learning Outcomes

## Overview
By completing this unit, you will learn how to customize Python's built-in behavior for your custom objects. You will master "Dunder" (Double Underline) methods to enable intuitive syntax like printing, indexing, comparison, and calling objects as functions.

**Estimated Time**: 4-5 hours total
- Knowledge: 45 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs: 2-3 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** what "Dunder" methods are and why they are called "hooks".
- [ ] **Explain** the difference between `__str__` (user-facing) and `__repr__` (developer-facing).
- [ ] **Understand** how Python translates operators (like `+`, `==`, `len()`) into dunder method calls.
- [ ] **Describe** the concept of "operator overloading" in Python.

### Object Representation & Identification

- [ ] **Implement** `__str__` to provide readable display names for objects.
- [ ] **Implement** `__repr__` to provide unambiguous debugging strings.
- [ ] **Ensure** that `repr()` output can ideally be used to recreate the object.

### Container & Sequence Behavior

- [ ] **Implement** `__len__` to allow objects to use the `len()` function.
- [ ] **Implement** `__getitem__` and `__setitem__` to enable bracket notation (`obj[key]`).
- [ ] **Enable** objects to behave like lists, dictionaries, or custom collections.

### Comparison & Boolean Logic

- [ ] **Implement** `__eq__` for value-based equality checking.
- [ ] **Implement** `__lt__`, `__gt__`, and other rich comparison methods.
- [ ] **Define** custom sorting behavior for lists of objects using comparison dunders.

### Callable Objects

- [ ] **Implement** `__call__` to allow an instance to be used like a function.
- [ ] **Use** callable objects to maintain state between "function" calls.

### Real-World Application

- [ ] **Create** a medical record system that allows patient lookup via `history[date]`.
- [ ] **Develop** a priority queue where patient objects are automatically sorted by severity.
- [ ] **Implement** validation engines that behave like functions but store complex configuration state.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all drills in `unit_3_4_special_methods_exercises.py`.
- Correct implementation of string representations and comparisons.
- Logic passes all unit tests for container behaviors.

### App Labs (Pass: 80% or higher)
- **Intuition**: Dunder methods are used to make the class interface "Pythonic" and clean.
- **Robustness**: Error handling in `__getitem__` for missing keys/indexes.
- **Testing**: All automated test cases pass for logical behavior.

---

## Next Steps

After mastering special methods:
1. **Move to Unit 3.1: Inheritance** to start the Advanced OOP series.
2. **Review** how dunder methods facilitate Polymorphism in Unit 3.2.
3. **Explore** more advanced dunders like `__enter__` and `__exit__` in the context of Exception Handling (Unit 4).

---

## Common Pitfalls to Avoid

✅ **Do**: Use `__str__` for pretty-printing and `__repr__` for logging/debugging.  
❌ **Don't**: Change the actual value of an object inside a comparison or representation method.

✅ **Do**: Use dunder methods to make your code more "Pythonic".  
❌ **Don't**: Overuse them where a simple named method (like `.calculate()`) would be clearer.

✅ **Do**: Check types in comparison methods before comparing values.  
❌ **Don't**: Assume `other` is always the same type as `self`.

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Explain the difference between `__str__` and `__repr__`?
2. Make a class that can be used like a dictionary (`obj['key']`)?
3. Define how two custom objects should be compared using `>`?
4. Explain what happens when you call `len(my_object)` if `__len__` is not defined?
5. Create a class that "remembers" how many times it has been called like a function?

If you answered "yes" to all, you're ready to proceed! 🎉
