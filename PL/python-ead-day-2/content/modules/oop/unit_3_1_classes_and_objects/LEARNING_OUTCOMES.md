# Unit 3.1: Classes and Objects - Learning Outcomes

## Overview
By completing this unit, you will master the foundations of Object-Oriented Programming (OOP) in Python. You will learn to transition from procedural code to an object-oriented mindset, building blueprints (Classes) and creating concrete data structures (Objects) that encapsulate both state and behavior.

**Estimated Time**: 5-6 hours total
- Knowledge: 40 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs (Easy, Intermediate, Advanced): 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** the core concepts of OOP: Classes, Objects, and Instances.
- [ ] **Explain** the "Blueprint vs. Building" analogy.
- [ ] **Articulate** the benefits of Encapsulation for data integrity.
- [ ] **Differentiate** between procedural and object-oriented programming paradigms.

### Class Definition & Instantiation

- [ ] **Define** a new class using the `class` keyword and `PascalCase` naming.
- [ ] **Assign** docstrings to classes for professional documentation.
- [ ] **Create** multiple independent instances of a class.
- [ ] **Inspect** object types using `type()` and `isinstance()`.

### Attributes & State

- [ ] **Implement** the `__init__` constructor to initialize object state.
- [ ] **Use** the `self` parameter correctly to represent the specific instance.
- [ ] **Define** Instance Variables that store data unique to each object.
- [ ] **Define** Class Variables that store shared state across all objects.
- [ ] **Distinguish** between shared class data and local instance data.

### Identity & Equality

- [ ] **Understand** that every object has a unique memory address (identity).
- [ ] **Compare** objects using the `is` operator for identity.
- [ ] **Compare** objects using the `==` operator for logical equality (and understand its default behavior).
- [ ] **Analyze** how multiple variables can point to the same object reference.

### Best Practices

- [ ] **Apply** the Single Responsibility Principle to class design.
- [ ] **Properly** initialize all attributes within the constructor.
- [ ] **Use** meaningful attribute names that reflect the real-world entity.
- [ ] **Minimize** global state by encapsulating logic within classes.

### Real-World Application

- [ ] **Model** a `Patient` class to consolidate demographic and clinical data.
- [ ] **Represent** a `MedicalDevice` with state (On/Off) and metadata (Serial Number).
- [ ] **Manage** a collection of objects (Registry) to simulate a hospital database.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all 6 concept drills in `unit_3_1_classes_and_objects_exercises.py`.
- Correct use of `__init__`, `self`, and variable scoping.
- Code follows PEP 8 conventions.

### App Labs (Pass: 80% or higher)
- **Functionality**: Classes correctly model the healthcare requirements.
- **Code Quality**: Proper use of instance vs. class variables.
- **Testing**: Passing all `unittest` cases in `tests.py`.

---

## Next Steps

After mastering classes and objects:
1. **Move to Unit 2.2: Methods** to learn about different types of class behaviors.
2. **Explore Unit 2.3: Encapsulation** for data hiding and property decorators.
3. **Study Unit 2.4: Special Methods** to customize object behavior (Dunder methods).

---

## Common Pitfalls to Avoid

✅ **Do**: Use `PascalCase` for class names: `class MedicalScanner`.  
❌ **Don't**: Use `snake_case` for classes: `class medical_scanner`.

✅ **Do**: Always include `self` as the first parameter in instance methods.  
❌ **Don't**: Forget `self`, which causes `TypeError` when calling methods.

✅ **Do**: Initialize unique data in `__init__`.  
❌ **Don't**: Use mutable class variables (like lists) for instance-specific data (causes data leakage).

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Create a class with 3 instance variables and 1 class variable?
2. Explain exactly what the `self` parameter represents?
3. Create 50 objects in a loop and store them in a list?
4. Explain why `obj1 is obj2` is False even if they have the same data?
5. Identify a scenario where a Class Variable is better than an Instance Variable?

If you answered "yes" to all, you're ready to proceed! 🎉
