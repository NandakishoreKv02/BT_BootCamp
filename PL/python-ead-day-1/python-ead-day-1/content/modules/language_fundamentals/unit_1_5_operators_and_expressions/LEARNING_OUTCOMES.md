# Unit 1.5: Operators & Expressions - Learning Outcomes

## Overview
In this unit, you will master Python's wide range of operators. Operators are special symbols that perform computations on data. You'll learn how to perform calculations, compare values, combine logical conditions, and use shorthand assignments. You will also understand the rules of precedence that determine how complex expressions are evaluated.

**Estimated Time**: 8-10 hours
- Knowledge: 90 min
- Exercises: 3 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Arithmetic Operators
- [ ] **Perform** basic math using `+`, `-`, `*`, `/`.
- [ ] **Utilize** floor division (`//`), modulus (`%`), and exponentiation (`**`) for specific calculations like medication dosage and patient cycle timing.
- [ ] **Explain** the difference between standard division and floor division.

### Comparison Operators
- [ ] **Evaluate** relationships between values using `==`, `!=`, `<`, `>`, `<=`, `>=`.
- [ ] **Apply** comparison for healthcare thresholds (e.g., checking if a vital sign is in a danger zone).

### Logical Operators
- [ ] **Combine** Boolean conditions using `and`, `or`, and `not`.
- [ ] **Understand** and leverage **short-circuit evaluation** for efficient and safe logic.
- [ ] **Construct** complex logical expressions for multi-variable clinical triggers.

### Assignment & Identity Operators
- [ ] **Use** augmented assignment operators (`+=`, `-=`, `*=`, etc.) for cleaner code.
- [ ] **Distinguish** between equality (`==`) and identity (`is`).
- [ ] **Explain** why `is` should be used when comparing to `None`.

### Membership Operators
- [ ] **Check** for the presence of elements in sequences (strings, lists) using `in` and `not in`.
- [ ] **Use** membership checks for rapid data validation (e.g., checking if a blood type is in an approved list).

### Precedence & Associativity
- [ ] **Evaluate** complex expressions correctly by following **PEMDAS** and Python's operator precedence rules.
- [ ] **Use** parentheses `()` to override default precedence and improve code clarity.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct calculation of medical formulas (e.g., fluid rates, clearance).
- Accurate use of logic for clinical decision-making scenarios.
- Proper application of membership and identity checks.
- Zero precedence-related logic errors in complex expressions.

### App Labs (Pass: 80% or higher)
- **Mathematical Accuracy**: Correct implementation of formulas with proper operator usage.
- **Logical Clarity**: Clean, readable Boolean expressions without redundant checks.
- **Safety**: Using `is None` for null checks and safe membership checks.
- **Style**: Adhering to PEP 8 spacing around operators (e.g., `x = a + b` vs `x=a+b`).

---

## Next Steps
1. **Unit 1.6: Control Flow Statements** will use these operators to create branches and loops in your code.

---

## Common Pitfalls to Avoid
✅ **Do**: Use parentheses for clarity in complex expressions (e.g., `(a and b) or c`).

❌ **Don't**: Rely solely on operator precedence for readability.

✅ **Do**: Use `val is None` to check for None.

❌ **Don't**: Use `val == None` (though it often works, `is` is the standard).

✅ **Do**: Remember that `/` always returns a `float` in Python 3.

❌ **Don't**: Expect integer division from `/` (use `//` instead).

✅ **Do**: Be careful with modulo `%` for negative numbers.

❌ **Don't**: Assume `and` has higher precedence than `or` without double-checking (it does, but parentheses are better).

✅ **Do**: Use `in` for checking membership in a list or string.

❌ **Don't**: Manually loop through a list to check if an item exists when `in` is available.
