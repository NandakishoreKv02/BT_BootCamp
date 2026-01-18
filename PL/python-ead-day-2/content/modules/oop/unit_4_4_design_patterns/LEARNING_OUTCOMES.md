# Unit 4.4: Design Patterns - Learning Outcomes

## Overview
By completing this unit, you will master the implementation of enterprise-grade architectural patterns in Python. You will learn to use Creational patterns (Singleton, Factory) and Behavioral patterns (Observer, Strategy) to build flexible, maintainable, and highly scalable medical software systems that adhere to industry best practices.

**Estimated Time**: 6-7 hours total
- Knowledge: 60 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs: 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Explain** the purpose and benefits of using Design Patterns in enterprise software.
- [ ] **Identify** the difference between Creational, Structural, and Behavioral patterns.
- [ ] **Understand** the "Single Responsibility Principle" as applied to pattern architecture.
- [ ] **Describe** the trade-offs of using certain patterns (e.g., global state in Singletons).

### Creational Patterns

- [ ] **Implement** the **Singleton** pattern to manage shared resources like database connections or configurations.
- [ ] **Apply** the **Factory** pattern to decouple object creation from the underlying business logic.
- [ ] **Use** decorators or metaclasses to simplify pattern implementation in Python.

### Behavioral Patterns

- [ ] **Implement** the **Observer** pattern to build reactive systems (e.g., patient vital alert broadcasts).
- [ ] **Develop** the **Strategy** pattern to switch between different clinical algorithms or billing rules at runtime.
- [ ] **Design** event-driven architectures where disparate components communicate via "Subjects" and "Observers".

### Real-World Application

- [ ] **Build** a centralized Hospital Configuration Manager using a thread-safe Singleton.
- [ ] **Develop** a Diagnostic Tool Factory that instantiates specific scanner logic (MRI, CT, X-Ray) based on input data.
- [ ] **Implement** an Emergency Alert System where multiple departments (ICU, Pharmacy, Security) react to a single "Code Blue" event using the Observer pattern.
- [ ] **Architect** a dosage calculation engine that uses a Strategy pattern to handle pediatric vs. geriatric rules.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all 10 drills in `unit_4_4_design_patterns_exercises.py`.
- Correct implementation of a Singleton with instance persistence.
- Successful use of a Strategy interface to swap math logic dynamically.

### App Labs (Pass: 80% or higher)
- **Flexibility**: The system can be extended with new logic without modifying core engine code (Open-Closed Principle).
- **Decoupling**: Classes do not have hard dependencies on concrete implementations of their helpers.
- **Testing**: All automated test cases pass for complex pattern interactions.

---

## Next Steps

After mastering design patterns:
1. **Move to Module 4: Exception Handling** to learn how to make these robust patterns resilient to runtime errors.
2. **Review** a production codebase (like Django or Flask) to identify these patterns in the wild.
3. **Explore** more complex patterns like Decorator (structural), Command, or State patterns.

---

## Common Pitfalls to Avoid

✅ **Do**: Use the Factory pattern when you have many subclasses and creation logic is complex.  
❌ **Don't**: Use a Factory for every object; simple `__init__` calls are fine for standard data objects.

✅ **Do**: Use a Singleton for truly global resources (Hardware drivers, Logging systems).  
❌ **Don't**: Use a Singleton just as a "convenient" way to access global variables; it makes testing difficult.

✅ **Do**: Ensure Observers are detached when no longer needed to prevent memory leaks.  
❌ **Don't**: Let the "Subject" know too much about the "Observer's" internal logic.

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Explain the difference between a "Simple Factory" and a "Factory Method"?
2. Write a Singleton class in Python that ensures only one instance ever exists?
3. Describe a scenario in a hospital where the Strategy pattern would prevent an `if/else` explosion?
4. Implement a Subject that notifies multiple Observers when its state changes?
5. Why is the Singleton pattern sometimes called an "Anti-Pattern"?

If you answered "yes" to all, you're ready to proceed! 🎉
