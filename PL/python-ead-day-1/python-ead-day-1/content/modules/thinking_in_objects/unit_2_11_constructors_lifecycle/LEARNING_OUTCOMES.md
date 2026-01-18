# Unit 2.11: Constructors & Object Lifecycle - Learning Outcomes

## Overview
This unit moves beyond simple class definitions to explore the mechanics of how objects are born and initialized. You will learn how to design flexible constructors that can handle various clinical scenarios through optional parameters and default values, ensuring that your objects always enter the system in a valid, "Use-ready" state.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 2 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Distinguish between Creation (__new__) and Initialization (__init__)**: Understand when each is called in the object lifecycle.
- [ ] **Explain the role of Default Parameters**: Use them to simplify object creation for standard cases while allowing customization.
- [ ] **Describe the danger of Mutable Default Arguments**: Why you should never use `def __init__(self, items=[])`.
- [ ] **Identify Initialization Best Practices**: Keep constructors lightweight and focused on state setup.

### Implementation Skills
- [ ] **Build Parameterized Constructors** that map complex inputs to object attributes.
- [ ] **Implement Optional Parameters** for clinical entities (e.g., an optional `insurance_provider` field).
- [ ] **Design Multi-stage Initialization** for objects that require internal validation during setup.
- [ ] **Use None as a sentinel value** for optional collections in constructors.

### Clinical System Design
- [ ] **Code a Medication class** that handles both mandatory data (name) and optional notes.
- [ ] **Develop an Admission record** that automatically sets the `admission_time` if not provided.
- [ ] **Implement a Surgeon object** that can be initialized with a variable list of specialties.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of default values for optional parameters.
- Successful handling of None-checked lists vs. mutable defaults.
- Zero runtime errors during varied instantiation patterns.

### App Labs (Pass: 80% or higher)
- **Flexibility**: The class can be instantiated with different combinations of arguments.
- **Robustness**: The object is correctly initialized even when optional data is missing.
- **Standards**: Proper usage of `__init__` according to Pythonic best practices.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Exploring how constructors are leveraged in patterns like Factories and Singletons.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `None` as a default for lists and initialize them inside `__init__`.

❌ **Don't**: Use a list literal `[]` in the parameter line (e.g., `def __init__(self, data=[])`) to avoid data leaking between objects.

✅ **Do**: Use keyword arguments for clarity when creating objects with many optional parameters.

❌ **Don't**: Perform heavy I/O (like reading a file) inside a constructor. It makes testing and object creation slow and brittle.
