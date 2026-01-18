# Unit 1.11: Python Coding Standards & Best Practices - Learning Outcomes

## Overview
Writing code that "works" is only half the battle. In professional software development, especially in healthcare where systems are audited and maintained for decades, code must be readable, standard-compliant, and "Pythonic." This unit introduces the PEP 8 standard and the best practices that transform a amateur script into professional software.

**Estimated Time**: 10-12 hours
- Knowledge: 2 hours
- Exercises: 4 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Standards & Naming
- [ ] **Explain** the importance of PEP 8 in the Python ecosystem.
- [ ] **Apply** professional naming conventions:
  - `snake_case` for variables and functions.
  - `PascalCase` for classes.
  - `SCREAMING_SNAKE_CASE` for constants.
- [ ] **Organize** imports according to standard groupings (Standard library, Third-party, Local).

### Readability & Structure
- [ ] **Format** code with correct indentation (4 spaces) and appropriate whitespace.
- [ ] **Implement** line-length limits (typically 79-88 characters) for better vertical reading.
- [ ] **Structure** files with clear headers, imports, and `if __name__ == "__main__":` blocks.

### "Pythonic" Thinking
- [ ] **Identify** and write "Pythonic" alternatives to common patterns (e.g., using `in` for membership checks).
- [ ] **Explain** the "Zen of Python" principles (e.g., "Simple is better than complex").
- [ ] **Evaluate** code for "Code Smells" and refactor for maintainability.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct refactoring of "bad" variable names to PEP 8 standards.
- Proper class and function definition syntax according to style guides.
- Implementation of clean internal spacing in expressions.

### App Labs (Pass: 80% or higher)
- **Compliance**: The code must pass a mental or automated PEP 8 check.
- **Self-Documentation**: Choosing names so descriptive that comments are rarely needed.
- **Maintainability**: Breaking large, messy functions into small, well-named units.
- **Consistency**: Maintaining the same style throughout the entire project.

---

## Next Steps
1. **Module 1.12: Hands-on Labs & Exercises**: A comprehensive review of all fundamentals.
2. **Module 2: Intermediate Python**: Applying these standards to advanced libraries.

---

## Common Pitfalls to Avoid
✅ **Do**: Use 4 spaces for indentation.

❌ **Don't**: Mix tabs and spaces; it causes confusing runtime errors.

✅ **Do**: Use verbs for function names (e.g., `calculate_risk`) and nouns for variables (`patient_age`).

❌ **Don't**: Use single-letter names like `x`, `y`, `z` unless they are for simple math coordinates or loop counters.

✅ **Do**: Place imports at the very top of the file.

❌ **Don't**: Import modules inside functions unless there is a very specific performance reason.

✅ **Do**: Keep code simple. If it's too clever to be easily read, it's probably not Pythonic.

❌ **Don't**: Over-comment. Comments should explain *why*, code should explain *how*.
