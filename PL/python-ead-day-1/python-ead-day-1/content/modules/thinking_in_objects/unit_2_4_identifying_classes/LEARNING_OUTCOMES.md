# Unit 2.4: Identifying Classes - Learning Outcomes

## Overview
This unit transitions from the syntax of classes to the **design** of classes. You will learn how to look at a paragraph of requirements and determine exactly which classes need to exist. We will explore the Noun-Verb technique, the BCE (Boundary-Control-Entity) pattern, and the vital skill of preventing "God Objects"—overly complex classes that try to do everything.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 3-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### System Analysis
- [ ] **Extract** potential classes (Nouns) and methods (Verbs) from raw clinical business requirements.
- [ ] **Apply** the Noun-Verb Analysis technique to filter out "candidate" classes from "fake" classes.
- [ ] **Categorize** classes using the BCE (Boundary, Control, Entity) model.

### Object Modeling
- [ ] **Differentiate** between persistent data (Entities), user interfaces (Boundaries), and process logic (Controllers).
- [ ] **Decompose** a "God Object" (a class that does too much) into smaller, highly cohesive classes.
- [ ] **Refine** class candidates by checking for "High Cohesion" and "Low Coupling."

### Practical Design
- [ ] **Model** a multi-layered healthcare system (e.g., Triage, Pharmacy, Billing) into a stable class diagram.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct identification of Nouns vs. Verbs in a clinical scenario.
- Successful classification of classes into Boundary, Control, or Entity.
- Identification of "God Object" smells in provided code snippets.

### App Labs (Pass: 80% or higher)
- **Modeling Precision**: Creating separate classes for data (Entity) and logic (Control).
- **Modularity**: Avoiding the "Main" function becoming a God Object by delegating to specific Controller classes.
- **BCE Implementation**: Correctly identifying a user-facing class (Boundary) versus a data-carrying class (Entity).

---

## Next Steps
1. **Unit 2.5: Information Hiding & Encapsulation**: Deep dive into `__private` attributes and getters/setters.

---

## Common Pitfalls to Avoid
✅ **Do**: Look for the "Entities" first—the things that survive even if the app is turned off (Patient, Invoice).

❌ **Don't**: Create a class for every single verb. "Printing" is a method, not a `PrinterBuilderManager` class.

✅ **Do**: Keep your classes focused. If a class name has "And" in it (e.g., `PatientAndBilling`), it's too big.

❌ **Don't**: Put user input/output inside an Entity class. A `Patient` shouldn't know how to `print()` itself to a console.
