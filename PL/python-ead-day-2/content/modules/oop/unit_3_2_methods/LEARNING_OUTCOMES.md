# Unit 3.2: Methods - Learning Outcomes

## Overview
By completing this unit, you will master the behavioral aspects of Object-Oriented Programming. You will learn to categorize logic correctly into instance, class, and static methods, handle complex parameter configurations, and manage the flow of data through return values and side effects.

**Estimated Time**: 5-6 hours total
- Knowledge: 45 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs (Easy, Intermediate, Advanced): 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** the difference between instance, class, and static methods.
- [ ] **Explain** the purpose of the `self` and `cls` parameters.
- [ ] **Understand** how Python handles method binding internally.
- [ ] **Describe** the concept of side effects vs. return values in clean code.

### Instance Methods

- [ ] **Implement** instance methods to modify an object's internal state.
- [ ] **Use** `self` to access and change instance attributes.
- [ ] **Design** methods that communicate with other methods within the same object.

### Class & Static Methods

- [ ] **Create** class methods using the `@classmethod` decorator for factory patterns.
- [ ] **Implement** static methods using the `@staticmethod` decorator for utility logic.
- [ ] **Determine** correctly when to use `@classmethod` vs. `@staticmethod`.

### Advanced Logic & Flow

- [ ] **Handle** method parameters using default arguments to simulate overloading.
- [ ] **Design** methods that return multiple values using tuples.
- [ ] **Manage** side effects (like console logging or database updates) without breaking object encapsulation.

### Best Practices

- [ ] **Apply** the Command-Query Separation principle in method design.
- [ ] **Write** clear, self-documenting method names following PEP 8.
- [ ] **Use** docstrings to explain method behavior and intended side effects.

### Real-World Application

- [ ] **Build** a multi-source factory for healthcare record creation.
- [ ] **Implement** dosage calculators that adjust behavior based on patient state.
- [ ] **Develop** auditing methods that track system-wide events using class-level variables.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all 6 concept drills in `unit_3_2_methods_exercises.py`.
- Correct use of `@classmethod` and `@staticmethod` decorators.
- Code follows PEP 8 naming conventions.

### App Labs (Pass: 80% or higher)
- **Functionality**: Methods correctly implement the required behavior.
- **Architecture**: Logic is appropriately distributed between instance, class, and static levels.
- **Testing**: All automated test cases pass.

---

## Next Steps

After mastering methods:
1. **Move to Unit 2.3: Properties and Encapsulation** to learn how to protect your data.
2. **Explore Unit 2.4: Special Methods** to customize object syntax.
3. **Compare** instance and class behaviors in complex hierarchies.

---

## Common Pitfalls to Avoid

✅ **Do**: Use `self` consistently for anything involving object attributes.  
❌ **Don't**: Forget the decorator for class or static methods (causes TypeError).

✅ **Do**: Return a value if the method is intended to provide information.  
❌ **Don't**: Rely solely on side-effects for methods that are supposed to be "Queries".

✅ **Do**: Use class methods for object creation helpers.  
❌ **Don't**: Try to access instance data (`self`) from a class or static method.

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Explain why we use `@classmethod` instead of just a regular method?
2. Create a static method that validates a string without using any class data?
3. Convert a method that has too many side effects into multiple atomic ones?
4. Call a class method using both the class name and an instance name?
5. Explain what happens if you try to use `self` inside a `@staticmethod`?

If you answered "yes" to all, you're ready to proceed! 🎉
