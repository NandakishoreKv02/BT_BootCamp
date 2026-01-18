# Unit 5.3: Custom Exceptions - Learning Outcomes

## Overview
Move beyond Python's built-in errors and learn to design your own domain-specific exception hierarchy. This unit covers how to create, name, and organize custom exception classes to make your application code more expressive, easier to debug, and capable of handling complex business logic failures distinct from system crashes.

**Estimated Time**: 6-8 hours
- Knowledge: 60 min
- Exercises: 90-120 min
- App Labs: 4-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Class Design
- [ ] **Define** custom exception classes by inheriting from Python's `Exception` class.
- [ ] **Implement** custom `__init__` methods to enrich exceptions with additional context (e.g., `user_id`, `error_code`).
- [ ] **Follow** PEP 8 naming conventions (suffixing with `Error`).

### Architectural Patterns
- [ ] **Structure** a tiered exception hierarchy (Base Error -> Specific Errors) to allow coarse or fine-grained catching.
- [ ] **Decide** when to use a custom exception versus a built-in one (e.g., `PatientNotFound` vs `ValueError`).

### Real-World Application (Healthcare)
- [ ] **Model** domain failures like `InsuranceDeclinedError` or `DrugInteractionWarning`.
- [ ] ** Serialize** custom exceptions into API responses or log formats.
- [ ] **Enforce** strict business rules using exceptions as control flow signals.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct inheritance from `Exception`.
- Ability to pass and store custom arguments in the exception.
- Demonstrating the ability to catch a parent custom exception to handle multiple child exceptions.

### App Labs (Pass: 80% or higher)
- **Expressiveness**: Errors must carry useful data (like which specifically failed), not just a message string.
- **Hierarchy**: Must use a base class (e.g., `AppError`) for all app-specific exceptions.
- **Clarity**: Raised exceptions must accurately describe the business failure.

---

## Next Steps
1. **Move to Module 5: File I/O** (or next module in sequence) to apply these patterns in reading/writing large datasets.
2. **Refactor** previous labs to use custom exceptions instead of generic `ValueError`.

---

## Common Pitfalls to Avoid
✅ **Do**: Inherit from `Exception` (or a custom base) for application errors.
❌ **Don't**: Inherit from `BaseException` (this prevents your error from being caught by `except Exception`).

✅ **Do**: Call `super().__init__(message)` in your custom init method to ensure standard behavior works.
❌ **Don't**: Overcomplicate exceptions with heavy logic. They should primarily be data carriers.

---

## Self-Assessment Questions
1. Why should you create a base exception class for your library/application?
2. What is the benefit of `except MyModuleError:` over `except Exception:`?
3. How do you add a custom attribute (like `retry_after`) to an exception?
