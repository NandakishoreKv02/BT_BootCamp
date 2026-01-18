# Unit 2.5: Attributes and Methods - Learning Outcomes

## Overview
This unit dives deep into the internal mechanics of a class. You will learn to distinguish between the **State** of an individual object (Instance Attributes) and the **Shared Knowledge** of the entire class (Class Attributes). You will also master professional method design, focusing on clear signatures and the principle of High Cohesion.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 3-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Distinguish** between Instance Attributes (unique to each object) and Class Attributes (shared by all).
- [ ] **Define** Method Signatures and explain why consistent naming/typing matters.
- [ ] **Identify** "Cohesion" within a class and explain its impact on maintenance.

### Implementation Skills
- [ ] **Declare** and use class-level variables for shared data (e.g., Hospital name, tax rates).
- [ ] **Design** instance methods that take multiple arguments to perform clinical logic.
- [ ] **Apply** proper naming conventions (`snake_case`) for attributes and methods.

### Clinical System Design
- [ ] **Model** a medical entity where some data is individual (Heart Rate) and some is institutional (Threshold Limits).
- [ ] **Evaluate** a class for cohesion, refactoring disjointed behaviors into separate modules.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct usage of `self.attr` vs `ClassName.attr`.
- Successful implementation of methods with specific signatures and return types.
- Identification of low-cohesion "smells" in provided clinical classes.

### App Labs (Pass: 80% or higher)
- **Shared State**: Using class attributes to track institutional stats (e.g., total patients admitted).
- **Signature Precision**: Methods accept clear, descriptive arguments and return logical medical outcomes.
- **Cohesion**: Class members are logically related to the central entity.

---

## Next Steps
1. **Unit 2.6: Information Hiding & Encapsulation**: Protecting internal state with private attributes.

---

## Common Pitfalls to Avoid
✅ **Do**: Use Class Attributes for constants that apply to *every* object (e.g., `MIN_TEMP = 95`).

❌ **Don't**: Modify a Class Attribute if you only intended to change one specific object—you'll affect the whole system.

✅ **Do**: Keep your method signatures small (2-3 arguments max where possible).

❌ **Don't**: Put a `calculate_paycheck()` method inside a `Patient` class (Low Cohesion).
