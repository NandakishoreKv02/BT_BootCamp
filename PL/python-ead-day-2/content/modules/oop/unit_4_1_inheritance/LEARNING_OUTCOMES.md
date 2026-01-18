# Unit 4.1: Inheritance - Learning Outcomes

## Overview
By completing this unit, you will master the principles of class hierarchies and code reuse. You will learn to build extensible systems using single and multiple inheritance, manage method resolution order (MRO), and use Abstract Base Classes to define strict architectural contracts.

**Estimated Time**: 6-7 hours total
- Knowledge: 60 min
- Check Your Understanding: 20 min
- Exercises: 2 hours
- App Labs: 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** the "Is-A" relationship and how it differs from "Has-A" (Composition).
- [ ] **Explain** the purpose of the `super()` function in initialization and method extension.
- [ ] **Understand** how Method Resolution Order (MRO) works in multiple inheritance.
- [ ] **Describe** the purpose of Abstract Base Classes (ABCs) as interface definitions.

### Basic & Hierarchy Management

- [ ] **Implement** single inheritance to create specialized child classes.
- [ ] **Use** `super().__init__` to propagate setup through the hierarchy.
- [ ] **Override** methods to change or extend behavior in subclasses.

### Advanced Inheritance

- [ ] **Implement** multiple inheritance to combine functionality from several parents.
- [ ] **Navigate** complex MRO scenarios using `Class.mro()` or `help(Class)`.
- [ ] **Avoid** the "Diamond Problem" through careful hierarchy design.

### Abstract Base Classes (Contract Enforcement)

- [ ] **Create** abstract classes using the `abc` module.
- [ ] **Define** mandatory interfaces using the `@abstractmethod` decorator.
- [ ] **Ensure** that subclasses comply with a fixed set of expectations.

### Design Principles

- [ ] **Apply** the Liskov Substitution Principle (LSP) in inheritance design.
- [ ] **Determine** when to favor Composition over Inheritance.
- [ ] **Write** extensible code that follows the Open/Closed Principle.

### Real-World Application

- [ ] **Build** a hospital staff hierarchy with shared base logic for names and IDs.
- [ ] **Implement** procedural standards using ABCs to force all medical tests to have specific outcomes.
- [ ] **Develop** multi-role manager classes using multiple inheritance (e.g., a Chief Medical Officer who is both a Doctor and an Admin).

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all drills in `unit_4_1_inheritance_exercises.py`.
- Correct use of `super()` in multi-level hierarchies.
- Proper implementation of abstract method overrides.

### App Labs (Pass: 80% or higher)
- **Hierarchy Clarity**: The "Is-A" relationships are logical and not forced.
- **Composition Implementation**: Correct refactoring from inheritance to composition in expert labs.
- **Testing**: All automated test cases pass, including MRO-based verification.

---

## Next Steps

After mastering inheritance:
1. **Move to Unit 3.2: Polymorphism** to see how these hierarchies enable flexible code.
2. **Review Unit 3.3: Advanced OOP Concepts** for Mixins and Dataclasses.
3. **Analyze** your code to ensure no inheritance trees are deeper than 3-4 levels.

---

## Common Pitfalls to Avoid

✅ **Do**: Use inheritance only for strict "Is-A" relationships.  
❌ **Don't**: Inherit just to get access to a single helper method (use composition or mixins).

✅ **Do**: Always call `super().__init__()` if you define a constructor in a child class.  
❌ **Don't**: Manually call `Parent.__init__(self)` as it breaks in multiple inheritance chains.

✅ **Do**: Keep your inheritance trees shallow (2-3 levels preferred).  
❌ **Don't**: Create "God Classes" at the top of a deep, complex hierarchy.

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Explain the difference between Inheritance and Composition?
2. Write a child class that calls its parent's method *after* doing its own logic?
3. Find the Method Resolution Order (MRO) of any given class?
4. Explain why you cannot instantiate an Abstract Base Class?
5. Identify a scenario where multiple inheritance is better than a deep single inheritance chain?

If you answered "yes" to all, you're ready to proceed! 🎉
