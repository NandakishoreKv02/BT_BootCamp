# Unit 2.10: Access Control & Encapsulation - Learning Outcomes

## Overview
In medical software, data integrity is a matter of safety. This unit teaches you how to shield an object's internal state from authorized or accidental modification. You will learn the Pythonic way to implement "Private" and "Protected" members, and how to use the `@property` decorator to create controlled interfaces for sensitive clinical data.

**Estimated Time**: 10-12 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 5-7 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define Encapsulation** and its importance in maintaining data invariants (e.g., preventing a heart rate from being set to -5).
- [ ] **Contrast Public, Protected (`_`), and Private (`__`)** members in Python.
- [ ] **Explain Name Mangling**: How Python actually handles biological "private" members.
- [ ] **Justify the use of @property** over traditional getter/setter methods.

### Implementation Skills
- [ ] **Enforce Data Validation** within setter methods to filter invalid medical inputs.
- [ ] **Implement Read-Only Attributes** using the `@property` decorator without a setter.
- [ ] **Hide Implementation Details** by moving internal logic into private methods.
- [ ] **Apply Naming Conventions** consistently to signal internal vs. external usage to other developers.

### Clinical System Design
- [ ] **Protect Patient Identifiers** by making MRNs and Social Security Numbers private.
- [ ] **Architect a Dosage Calculator** that validates values before applying them to a prescription object.
- [ ] **Model a Bio-Registry** where sensors can only be updated through verified, encapsulated methods.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of single and double underscores for member visibility.
- Successful implementation of a property with both getter and setter logic.
- Prevention of illegal state changes via encapsulated validation.

### App Labs (Pass: 80% or higher)
- **Data Integrity**: Sensitive attributes cannot be modified directly from outside the class.
- **Syntactic Correctness**: Proper use of the `@property` and `.setter` decorators.
- **Interface Quality**: The class provides a clean, safe public interface while hiding complexity.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Using encapsulated objects as building blocks for enterprise design patterns.

---

## Common Pitfalls to Avoid
✅ **Do**: Use single underscore (`_`) for "Protected"—it's a convention telling developers "Please don't touch this from outside, but I won't stop you."

❌ **Don't**: Use double underscore (`__`) unless you absolutely must trigger name mangling (it can make debugging and testing harder).

✅ **Do**: Use `@property` for attributes that need validation or calculation upon access.

❌ **Don't**: Create getters and setters for *every* attribute. If a value has no validation rules, keep it public.
