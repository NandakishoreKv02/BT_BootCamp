# Unit 2.14: Static Members and Utility Behavior - Learning Outcomes

## Overview
Not everything in an object-oriented system belongs to a specific instance. Some data (like the total number of beds in a hospital) and some logic (like converting Celsius to Fahrenheit) are shared or global to the class itself. This unit teaches you how to manage "Class-Level" state and behavior using Static variables and specialized decorators.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 2 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define Static Variables**: Understand data that is shared across all instances of a class.
- [ ] **Distinguish between @staticmethod and @classmethod**: Know when logic requires class access (`cls`) versus no state access.
- [ ] **Understand the Concept of "Utility Behavior"**: When a function belongs in a class for organization but doesn't need personal object data.
- [ ] **Identify Factory Pattern Basics**: How to use class methods to provide alternative ways to create objects.

### Implementation Skills
- [ ] **Implement Class Counters**: Use static variables to track the number of objects created (e.g., `Patient.count`).
- [ ] **Develop Utility Classes**: Build tools for clinical unit conversion using `@staticmethod`.
- [ ] **Implement Factory Methods**: Use `@classmethod` to instantiate objects from different data formats (e.g., from a CSV string).
- [ ] **Manage Shared Configurations**: Practical use of static constants for hospital-wide settings.

### Clinical System Design
- [ ] **Build a Global Registry Tracker**: Maintain a live count of active ER admissions.
- [ ] **Design a Medical Unit Converter**: A stateless class for translating labs between Metric and Imperial.
- [ ] **Create a Flexible Patient Factory**: Initialize patients either via manual input or from a legacy data dictionary.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Accurate incrementing of a class-level variable.
- Correct syntax for `@staticmethod` returning valid calculation results.
- Successful implementation of a factory method returning a new class instance.

### App Labs (Pass: 80% or higher)
- **Shared State Integrity**: Demonstrating that changes to a static variable affect all instances.
- **Logical Grouping**: Properly placing utility logic in static methods rather than instance methods.
- **Architectural Patterns**: Correct use of `cls` in class methods to ensure inheritance friendliness.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Moving into Abstract Base Classes and Singletons.

---

## Common Pitfalls to Avoid
✅ **Do**: Use static variables for shared constants or global counters.

❌ **Don't**: Use static variables for data that *should* be unique to a patient (like their heart rate).

✅ **Do**: Use `@classmethod` if your factory needs to support inheritance (it uses `cls()` instead of the name).

❌ **Don't**: Overuse static methods; if a method needs to touch `self.name`, it MUST be an instance method.
