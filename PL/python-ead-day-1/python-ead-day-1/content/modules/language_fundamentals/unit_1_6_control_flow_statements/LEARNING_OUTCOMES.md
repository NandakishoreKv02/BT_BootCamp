# Unit 1.6: Control Flow Statements - Learning Outcomes

## Overview
Control flow statements are the backbone of program logic. In this unit, you will learn how to make decisions using conditionals and repeat tasks using loops. These concepts are essential for building intelligent healthcare applications, such as triage systems that categorize patients or batch processors that handle thousands of medical records.

**Estimated Time**: 10-12 hours
- Knowledge: 2 hours
- Exercises: 4 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Conditional Statements
- [ ] **Implement** decision tree logic using `if`, `elif`, and `else`.
- [ ] **Handle** multiple branches of logic for complex triage scenarios.
- [ ] **Use** nested conditions to drill down into specific data states while maintaining readability.

### Looping Constructs
- [ ] **Iterate** over patient collections and numeric ranges using `for` loops and `range()`.
- [ ] **Implement** polling and conditional repetition using `while` loops (e.g., waiting for a device response).
- [ ] **Explain** the difference between definite (for) and indefinite (while) iteration.

### Loop Control Mechanisms
- [ ] **Efficiently stop** loops using `break` when a search item is found.
- [ ] **Skip** invalid or irrelevant data points using `continue`.
- [ ] **Use** the `pass` statement as a placeholder for future implementation.

### Iteration Basics
- [ ] **Generate** sequences of numbers using `range()` with start, stop, and step parameters.
- [ ] **Manage** index-based and value-based iteration over healthcare datasets.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct implementation of multiple `elif` branches for vitals categorization.
- Accurate usage of `range()` to generate specific numeric sequences.
- Effective use of `break` and `continue` to manage loop execution.
- Creation of nested logic that correctly filters and processes data.

### App Labs (Pass: 80% or higher)
- **Modular Decision Making**: Using functions with parameters to drive control flow logic.
- **Data Safety**: Ensuring loops terminate correctly (no infinite loops).
- **Readability**: Keeping nested levels manageable and following PEP 8.
- **Logic Correctness**: Handling edge cases (empty lists, extreme vital values) using conditionals.

---

## Next Steps
1. **Module 2: Data Structures** will show you more complex containers to iterate over.
2. **Module 3: Functions** will teach you how to wrap this logic into reusable blocks.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `elif` for mutually exclusive conditions.

❌ **Don't**: Use multiple `if` statements when only one branch should execute.

✅ **Do**: Use `for` loops when you know the number of items or have a collection.

❌ **Don't**: Use a `while` loop with a counter when a `for` loop over `range()` is cleaner.

✅ **Do**: Ensure your `while` loop has a clear exit condition to avoid infinite loops.

❌ **Don't**: Forget to update the loop variable within a `while` loop body.

✅ **Do**: Keep nesting levels low (ideally < 3) to maintain code readability.

❌ **Don't**: Create deeply nested "if-within-if-within-for" blocks; consider refactoring into functions.

✅ **Do**: Use `range(start, stop)` and remember that `stop` is exclusive.

❌ **Don't**: Expect `range(1, 5)` to include the number 5.
