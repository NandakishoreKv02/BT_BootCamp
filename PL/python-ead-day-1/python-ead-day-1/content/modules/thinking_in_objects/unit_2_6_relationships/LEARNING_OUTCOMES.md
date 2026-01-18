# Unit 2.6: Relationships Between Classes - Learning Outcomes

## Overview
Classes in a large system are like specialized medical departments—they must work together to achieve a goal. This unit teaches you how to model these connections correctly using the industry-standard "Three Relationships": **Is-a** (Inheritance), **Has-a** (Composition/Aggregation), and **Uses** (Dependency). You will learn to choose the right one to avoid brittle, "spaghetti" architectures.

**Estimated Time**: 10-12 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 5-7 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define and Differentiate** between Inheritance (Is-a), Composition (Has-a), and Dependency (Uses).
- [ ] **Explain** the difference between Composition (strict ownership) and Aggregation (weak association).
- [ ] **Identify** common modeling mistakes, such as using inheritance when composition was appropriate.

### Implementation Skills
- [ ] **Code** a "Has-a" relationship by passing one object into the constructor of another.
- [ ] **Implement** a "Uses" relationship by passing an object as a method argument.
- [ ] **Implement** basic Inheritance ("Is-a") for specialized clinical entities.

### Clinical System Design
- [ ] **Model** a Hospital Ward that *has* Beds (Composition).
- [ ] **Model** a Doctor who *uses* a Stethoscope (Dependency).
- [ ] **Model** a Surgeon as a specialized type (Is-a) of Doctor.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct manual classification of relationships in clinical scenarios.
- Successful implementation of Composition vs. Aggregation in Python.
- Identification of "Inheritance Abuse" in provided architectural diagrams.

### App Labs (Pass: 80% or higher)
- **Structural Integrity**: Objects are correctly nested or linked based on the requirement.
- **Dependency Management**: Methods correctly accept object collaborators.
- **Modeling Choice**: Correct selection of Inheritance vs. Composition for specialized clinical equipment.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Polymorphism, Abstract Base Classes, and Design Patterns.

---

## Common Pitfalls to Avoid
✅ **Do**: Use "Is-a" (Inheritance) ONLY when the child class truly is a subtype (e.g., `Cardiologist` is a `Doctor`).

❌ **Don't**: Use Inheritance just to "steal" code. If a `Doctor` needs a `Printer`, don't make `Doctor` inherit from `Printer`. Use "Has-a".

✅ **Do**: Favor Composition over Inheritance. It's usually more flexible.

❌ **Don't**: Make everything a dependency. If a `Patient` *always* has a `HeartRateRecord`, make it a "Has-a" relationship in the constructor.
