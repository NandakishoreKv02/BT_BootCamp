# Unit 2.9: Representing Classes in Python - Learning Outcomes

## Overview
This unit focuses on the technical implementation and coding standards for objects in Python. You will learn the specific syntax that brings your conceptual models to life, adhering to global standards like PEP 8, and mastering the fundamental "Plumbing" of Python classes—constructors, self-reference, and method execution.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 2 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Explain PEP 8 Naming Conventions** for classes (PascalCase) and methods/attributes (snake_case).
- [ ] **Describe the Lifecycle of __init__**: When it is called and its role in object initialization.
- [ ] **Define 'self'**: Explain why every instance method requires `self` as the first parameter.

### Implementation Skills
- [ ] **Standardize Class Definitions** according to Python best practices.
- [ ] **Program Constructors** that correctly initialize state for clinical entities.
- [ ] **Differentiate between Class and Instance Scope** in Python syntax.
- [ ] **Invoke Methods** both internally (using self) and externally.

### Clinical System Design
- [ ] **Implement a standardized Patient class** with complete state initialization.
- [ ] **Develop a Physician registry** where objects are instantiated with specific behavioral signatures.
- [ ] **Code a LabTest request system** that utilizes clean, PEP 8 compliant method names.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Zero PEP 8 violations in class and method naming.
- Correct use of `self` in all instance methods.
- Successful instantiation of multiple objects with independent state.

### App Labs (Pass: 80% or higher)
- **Code Quality**: Adherence to Pythonic standards.
- **Initialization Logic**: `__init__` is used effectively to set up the object's starting state.
- **Interaction**: Methods communicate with each other correctly using instance scope.

---

## Next Steps
1. **Unit 2.10: Access Control & Encapsulation**: Learning how to protect the state you just learned to create.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `CamelCase` for class names (e.g., `InpatientRecord`).

❌ **Don't**: Use lower case or snake_case for class names (e.g., `inpatient_record`).

✅ **Do**: Remember that `self` is not a keyword (you could name it anything), but using anything other than `self` is a major violation of community standards.

❌ **Don't**: Forget the `()` when creating an object (e.g., `p = Patient` is a reference to the class, not an object).
