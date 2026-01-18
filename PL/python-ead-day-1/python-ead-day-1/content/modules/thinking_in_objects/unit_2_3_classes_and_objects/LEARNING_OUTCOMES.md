# Unit 2.3: Classes and Objects - Learning Outcomes

## Overview
This unit introduces the formal syntax of Object-Oriented Programming in Python. You will transform your conceptual understanding of "Objects" into concrete "Classes." We will explore the relationship between the static Blueprint (Class) and the dynamic Runtime Instance (Object), while mastering the three pillars of object existence: Identity, State, and Behavior.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 3-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define** a Class as a blueprint and an Object as a runtime instance.
- [ ] **Distinguish** between Object Identity (`id()`), State (attributes), and Behavior (methods).
- [ ] **Explain** the "Blueprint vs. Runtime" reality using real-world clinical analogies.

### Python Implementation
- [ ] **Construct** simple Python classes using the `class` keyword.
- [ ] **Initialize** objects using the `__init__` constructor methods.
- [ ] **Manipulate** object state through instance variables.
- [ ] **Trigger** behaviors using instance methods.

### Critical Thinking
- [ ] **Analyze** how multiple objects of the same class maintain independent identities.
- [ ] **Map** clinical entities (e.g., a Patient, a Medical Device) into formal class structures.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of `class` and `def __init__` syntax.
- Demonstration of understanding that `p1` and `p2` are distinct even with identical data.
- Successful mapping of State and Behavior to class members.

### App Labs (Pass: 80% or higher)
- **Object Modeling**: Creating classes that accurately represent healthcare entities.
- **State Integrity**: Ensuring methods correctly update attributes without side effects.
- **Behavior Logic**: Implementing logic inside methods that operates on the object's instance variables (`self`).

---

## Next Steps
1. **Unit 2.4: Attributes and Methods**: Deep dive into `self`, class versus instance data.

---

## Common Pitfalls to Avoid
✅ **Do**: Use PascalCase for Class names (e.g., `PatientRecord`).

❌ **Don't**: Forget the `self` parameter in method definitions—without it, your behaviors can't access your state.

✅ **Do**: Think of a class as the *idea* of a thing, and an object as the *actual* thing.

❌ **Don't**: Assume that two objects with identical data are "the same" thing (they have different identities).
