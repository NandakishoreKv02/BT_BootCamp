# Unit 2.1: From Procedural to Object-Oriented Thinking - Learning Outcomes

## Overview
This unit marks the beginning of a major paradigm shift. You are moving from writing "scripts" (lists of instructions) to building "systems" (collaborating objects). We will explore why procedural code becomes unmanageable at scale and how the Object-Oriented (OO) mindset solves these complexity problems by mirroring the real world.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 3-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Conceptual Understanding
- [ ] **Contrast** procedural programming with object-oriented programming.
- [ ] **Explain** the "Stateless Function vs. Stateful Object" distinction.
- [ ] **Identify** the breaking point where procedural code becomes "Spaghetti Code."
- [ ] **Define** the core benefit of OOP: managing complexity through encapsulation.

### Critical Analysis
- [ ] **Analyze** a real-world scenario (e.g., a Hospital) and identify key "Objects" (Patient, Doctor, Bed) vs. "Procedures" (admit, discharge).
- [ ] **Evaluate** code snippets to determine if they are procedural or object-oriented.
- [ ] **Decide** when NOT to use OOP (simple scripts, data pipelines).

### Code Transition (Python)
- [ ] **Refactor** simple global-state procedural code into encapsulated structures (using dictionaries as proto-objects).
- [ ] **Group** related data and functions conceptually before writing a single class.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct identification of procedural vs. OO characteristics.
- Successful refactoring of global variables into structured dictionaries/functions.
- Demonstrated ability to group "state" and "behavior" together.

### App Labs (Pass: 80% or higher)
- **Modularity**: Code is broken down into logical units (even if not yet classes).
- **Data Encapsulation**: Avoiding global keyword usage; passing state explicitly.
- **Modelling**: Choosing appropriate data structures that could become classes later.

---

## Next Steps
1. **Unit 2.2: Why Object-Oriented Programming?**: Deep dive into the four pillars of OOP.
2. **Unit 2.3: Classes and Objects**: Writing your first actual `class`.

---

## Common Pitfalls to Avoid
✅ **Do**: Think about "Nouns" (Entities) first, then "Verbs" (Behaviors).

❌ **Don't**: Start coding immediately by writing top-to-bottom scripts.

✅ **Do**: Recognize that dictionaries + functions are the bridge to OOP in Python.

❌ **Don't**: Assume OOP is just "putting functions inside classes" (that's just namespacing).

✅ **Do**: Use OOP for systems with complex state management.

❌ **Don't**: Force OOP on a simple 10-line calculation script.
