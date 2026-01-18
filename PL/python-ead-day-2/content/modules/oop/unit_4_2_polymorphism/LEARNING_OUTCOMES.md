# Unit 4.2: Polymorphism - Learning Outcomes

## Overview
By completing this unit, you will master Python's "Duck Typing" philosophy and the power of Polymorphism. You will learn to write flexible, extensible code that works with different types of objects as long as they provide the required behavior, and customize how standard operators behave for your custom types.

**Estimated Time**: 5-6 hours total
- Knowledge: 45 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs: 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** Polymorphism and how it manifests in Python.
- [ ] **Explain** the concept of "Duck Typing" ("If it walks like a duck...").
- [ ] **Understand** how inheritance-based polymorphism differs from runtime duck typing.
- [ ] **Describe** the mechanism of operator overloading using dunder methods.

### Flexible Programming (Duck Typing)

- [ ] **Write** functions and methods that accept any object with a required method/attribute.
- [ ] **Apply** the principle of "Ask for behavior, not for type".
- [ ] **Use** `try/except AttributeError` to handle dynamic object capabilities safely.

### Behavioral Overriding

- [ ] **Implement** polymorphic method signatures across unrelated classes.
- [ ] **Leverage** parental references to execute subclass-specific logic.
- [ ] **Design** generic collection handlers that process different object types uniformly.

### Operator Overloading

- [ ] **Implement** mathematical operators (`+`, `-`, `*`) for custom classes.
- [ ] **Implement** logic operators (`==`, `!=`, `<`, `>`) for value-based logic.
- [ ] **Ensure** operators behave intuitively according to the domain (e.g., adding two `Duration` objects).

### Architectural Interfaces

- [ ] **Use** Abstract Base Classes (ABCs) to enforce a common interface for polymorphic systems.
- [ ] **Design** plugin-style architectures where new classes can be "plugged in" without modifying existing code.

### Real-World Application

- [ ] **Build** a universal medical device interface that connects to any device implementing `get_reading()`.
- [ ] **Develop** an alerting system where different strategies (Threshold vs. Trend) can be swapped polymorphically.
- [ ] **Implement** monetary arithmetic that handles different currencies using operator overloading.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all 10 drills in `unit_4_2_polymorphism_exercises.py`.
- Correct implementation of complex duck-typing functions.
- Mathematical operations are correctly overloading dunder methods.

### App Labs (Pass: 80% or higher)
- **Flexibility**: The system can add a new "Device" or "Alert Strategy" with ZERO changes to the core engine.
- **Pythonic Style**: Use of `__sub__` and `__iter__` to make classes behave like standard Python types.
- **Testing**: All automated test cases pass for all 6 App Labs.

---

## Next Steps

After mastering polymorphism:
1. **Move to Unit 3.3: Advanced OOP Concepts** to learn about memory optimization and mixins.
2. **Apply** polymorphic patterns to your Final Project to make it more extensible.
3. **Explore** the Strategy Design Pattern (Unit 3.4) which relies heavily on polymorphism.

---

## Common Pitfalls to Avoid

✅ **Do**: Use polymorphism to eliminate long `if/elif` chains based on types.  
❌ **Don't**: Overload operators in a way that is confusing (e.g., using `+` for something that isn't additive).

✅ **Do**: Document the required "interface" (methods/attributes) for your duck-typed functions.  
❌ **Don't**: Forget to handle the case where an unexpected object is passed (AttributeError).

✅ **Do**: Use ABCs when you need strict interface enforcement.  
❌ **Don't**: Require inheritance if simple duck typing is sufficient for the task.

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Explain the phrase "If it walks like a duck and quacks like a duck, it's a duck"?
2. Write a function that calls `.render()` on any object without knowing its class?
3. Override the `-` operator for a class representing a `TimeSlot`?
4. Explain why polymorphism is key to the "Open/Closed Principle"?
5. Implement a "Strategy Pattern" where a `Monitor` object changes its behavior at runtime?

If you answered "yes" to all, you're ready to proceed! 🎉
