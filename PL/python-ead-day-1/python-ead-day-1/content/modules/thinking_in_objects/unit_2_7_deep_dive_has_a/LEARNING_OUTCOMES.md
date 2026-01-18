# Unit 2.7: Has-a Relationships – Deep Dive - Learning Outcomes

## Overview
Moving beyond simple containment, this unit explores the nuances of object associations. You will master the structural differences between **Composition** and **Aggregation**, implement various **Multiplicities** (how many objects connect to another), and understand **Lifecycle Ownership**—crucial for managing data integrity and memory in large-scale clinical applications.

**Estimated Time**: 10-12 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 5-7 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define Multiplicity** and explain the differences between One-to-One, One-to-Many, and Many-to-Many relationships.
- [ ] **Contrast** Composition and Aggregation in terms of "Lifecycle Ownership" (what happens when the container is deleted).
- [ ] **Explain Navigability** and how it affects the way objects access each other's data.

### Implementation Skills
- [ ] **Implement One-to-Many** relationships using Python lists or dictionaries.
- [ ] **Codify Lifecycle Rules** by using constructors for composition and setters for aggregation.
- [ ] **Represent Many-to-Many** associations using cross-referencing collections.

### Clinical System Design
- [ ] **Model** a Hospital Ward that strictly owns its Beds (1:N Composition).
- [ ] **Model** a Doctor-Patient relationship (M:N Aggregation).
- [ ] **Determine** if a clinical entity (e.g., SurgeryLog) should be a Composition or an Aggregation based on its lifecycle needs.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct implementation of list-based one-to-many relationships.
- Demonstration of object survival (Aggregation) vs. destruction (Composition).
- Logic challenges involving bidirectional navigability.

### App Labs (Pass: 80% or higher)
- **Multiplicity Precision**: Collections (list/dict) are used correctly to match required multiplicities.
- **Ownership Integrity**: Constructors and methods enforce the correct lifecycle relationship.
- **Domain Accuracy**: Scenarios correctly map real-world medical hierarchies to code structures.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Exploring how these relationships facilitate complex design patterns.

---

## Common Pitfalls to Avoid
✅ **Do**: Use a list for "One-to-Many" (e.g., `self.vitals = []`).

❌ **Don't**: Assume that just because an object is inside another, it will be automatically deleted. In Python, you must manage references carefully.

✅ **Do**: Use IDs or references for "Many-to-Many" to avoid circular reference issues.

❌ **Don't**: Use Composition for a relationship that should be temporary (e.g., a Surgeon shouldn't strictly "own" the surgical theatre).
