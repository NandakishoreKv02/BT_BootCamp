# Unit 2.15: Abstraction & Design Principles - Learning Outcomes

## Overview
Abstraction is the art of simplifying complexity. In this unit, you will learn how to define "Blueprints" that cannot be instantiated themselves but force child classes to follow a specific contract. You will also learn the Single Responsibility Principle (SRP), ensuring each class in your medical system does exactly one thing well.

**Estimated Time**: 10-14 hours
- Knowledge: 3 hours
- Exercises: 3 hours
- App Labs: 4-8 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Theory and Concepts
- [ ] **Define Abstraction**: Understand the process of hiding internal details and showing only essential features.
- [ ] **Explain Abstract Base Classes (ABC)**: Why we use them to prevent the creation of "Generic" medical objects.
- [ ] **Understand the Single Responsibility Principle (SRP)**: Why a `Patient` class shouldn't also send emails or generate PDFs.
- [ ] **Differentiate between Interface and Implementation**: Focusing on WHAT an object does rather than HOW it does it.
- [ ] **Analyze Clean Object Design**: Identifying "Codes Smells" in monolithic classes.

### Implementation Skills
- [ ] **Implement Abstract Base Classes** using Python's `abc` module and the `@abstractmethod` decorator.
- [ ] **Enforce Subclass Contracts**: Ensure all diagnostic tools implement a required `perform_scan()` method.
- [ ] **Refactor Monolithic Classes**: Break down a "God Object" into smaller, SRP-compliant components.
- [ ] **Apply Abstraction to APIs**: Create high-level methods that hide low-level mathematical or DB logic.

### Clinical System Design
- [ ] **Model an Abstract Medical Device**: Create a base for all scanners (MRI, CT, X-Ray).
- [ ] **Design an SRP-Compliant Billing System**: Separate patient data from cost calculation and invoice generation.
- [ ] **Architect a Multi-Channel Notification Engine**: Use abstraction to send alerts via SMS, Email, or Hospital Pager.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct usage of `ABC` and `@abstractmethod`.
- Demonstration of a `TypeError` when trying to instantiate an abstract class.
- Successful implementation of concrete subclasses that fulfill the abstract contract.

### App Labs (Pass: 80% or higher)
- **Design Integrity**: Classes demonstrate low coupling and high cohesion (SRP).
- **Contract Fulfillment**: Subclasses properly implement all abstract methods with meaningful clinical logic.
- **Complexity Management**: Effectively using abstraction to simplify a multi-step medical process.

---

## Next Steps
1. **Module 3: Advanced OOP Patterns**: Exploring Design Patterns like Singleton, Factory, and Strategy in depth.

---

## Common Pitfalls to Avoid
✅ **Do**: Use ABCs when you want to define a common interface for a group of related classes.

❌ **Don't**: Use Abstraction for every single class; if it's simple and concrete, keep it that way.

✅ **Do**: Keep classes focused. If you can't describe a class's purpose without using "and", it might be violating SRP.

❌ **Don't**: Forget to import `ABC` and `abstractmethod` from the `abc` module.
