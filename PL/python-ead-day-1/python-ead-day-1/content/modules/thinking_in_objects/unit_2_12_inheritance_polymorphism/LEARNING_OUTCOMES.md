# Unit 2.12: Inheritance & Polymorphism - Learning Outcomes

## Overview
Inheritance and Polymorphism are the dual engines of scalable object-oriented design. In this unit, you will learn how to build "Family Trees" of medical classes, allowing specialized clinical tools to inherit behavior from general ones. You will also master Polymorphism—the ability to interact with a set of diverse objects (like different types of therapy) as if they were the same, simplifying complex clinical workflows.

**Estimated Time**: 10-14 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 5-9 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define Inheritance** and the "Is-A" relationship (e.g., a Surgeon IS-A Physician).
- [ ] **Explain Method Overriding**: Why and how a child class provides a specialized version of a parent's method.
- [ ] **Understand the super() Keyword**: How to leverage parent class logic while adding new specialized behavior.
- [ ] **Define Polymorphism**: The concept of "Many Forms" where different objects respond to the same method call in their own way.
- [ ] **Identify Inheritance Pitfalls**: Recognize "Fragile Base Classes" and deep, confusing hierarchies.

### Implementation Skills
- [ ] **Create Class Hierarchies** using Python's `class Child(Parent):` syntax.
- [ ] **Extend Constructors** using `super().__init__()` to initialize base and derived attributes.
- [ ] **Override Base Methods** to provide specialized clinical logic (e.g., unique calibration for a specific laser).
- [ ] **Implement Polymorphic Loops** that process a list of diverse objects via a common method interface.

### Clinical System Design
- [ ] **Model Medical Occupations**: Build a hierarchy from `HospitalStaff` down to specific roles like `Oncologist`.
- [ ] **Implement Multi-modal Therapy Plans**: Use polymorphism to run a `execute()` method on Plans, Meds, and Exercises.
- [ ] **Architect a Generic Result System**: Create a base `LabResult` and override it for `BloodResult` and `ImagingResult`.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of parentheses for inheritance.
- Accurate usage of `super()` in overridden methods.
- Demonstration of polymorphic behavioral differences in a shared loop.

### App Labs (Pass: 80% or higher)
- **Code Reuse**: Effectively using parent class attributes and methods.
- **Specialization**: Properly overriding methods to meet specific subtype requirements.
- **Architectural Soundness**: Choosing a logical inheritance path that avoids "God Objects."

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Exploring Interfaces and Abstract Base Classes (ABCs) to enforce polymorphic contracts.

---

## Common Pitfalls to Avoid
✅ **Do**: Use inheritance only when a true "Is-A" relationship exists.

❌ **Don't**: Use inheritance just to share a few lines of code (prefer Composition if it's "Has-A").

✅ **Do**: Call `super().__init__()` at the start of your child class constructor.

❌ **Don't**: Create deep hierarchies (more than 3-4 levels) as they become extremely difficult to debug and maintain.
