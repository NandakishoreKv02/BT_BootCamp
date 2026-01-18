---
title: "Coding Standards: The Professional Standard"
type: knowledge
module: language_fundamentals
unit: unit_1_11_coding_standards
order: 11
difficulty: beginner
tags:
  subtopics:
    - pep8
    - naming-conventions
    - readability
    - pythonic-code
---

# Unit 1.11: Python Coding Standards & Best Practices

## 1. What
**Coding Standards** are a set of rules and guidelines for writing source code. They ensure that a project is consistent, readable, and maintainable by multiple developers. In Python, the definitive guide is **PEP 8 (Python Enhancement Proposal 8)**.

In healthcare, coding standards are not optional. Medical software is often mission-critical and highly regulated. Adhering to standards reduces the risk of bugs and makes it easier for security auditors to review the code for vulnerabilities.

---

## 2. Example

### Example 1: Naming Conventions
```python
# Constants (Screaming Snake Case)
MAX_PATIENT_TIMEOUT = 30 

# Classes (PascalCase)
class MedicalRecordManager:
    pass

# Variables & Functions (snake_case)
def calculate_dose(patient_weight):
    total_mg = 50 * patient_weight
    return total_mg
```

### Example 2: Non-Pythonic vs Pythonic
```python
# Non-Pythonic (looks like Java/C)
fruits = ["Apple", "Orange", "Grape"]
for i in range(len(fruits)):
    print(fruits[i])

# Pythonic (Clean, Readable)
for fruit in fruits:
    print(fruit)
```

### Example 3: Correct Spacing (PEP 8)
```python
# Bad: To much space or too little
x=calculate( a,b )

# Good: Standard spacing
x = calculate(a, b)
```

---

## 3. Explanation

### PEP 8 Highlights
- **Indentation**: Use 4 spaces per indentation level.
- **Line Length**: Limit all lines to a maximum of 79-88 characters.
- **Imports**: Put all imports at the top of the file, grouped by type.
- **Blank Lines**: Use two blank lines around top-level functions and classes.

### Naming Styles
1.  **`snake_case`**: All lowercase with underscores. Used for: Variables, Functions, Modules.
2.  **`PascalCase`**: (CapWords). Every word capitalized. Used for: Classes.
3.  **`SCREAMING_SNAKE_CASE`**: All uppercase with underscores. Used for: Constants (values that never change).

### "Pythonic" Principles
Being "Pythonic" means writing code that fits the idioms and culture of the Python language.
- **Explicit is better than implicit**: Don't be "too clever." Clearer code is better than "shorter" code.
- **Readability counts**: If code is hard to read, it's wrong—even if it works.
- **Membership**: Use `if "A" in list:` instead of manual looping to search.

---

## 4. Why

### Team Collaboration
If everyone follows the same style, a developer can join a new project and understand the code immediately. It eliminates "style arguments" during code reviews.

### Future You
You will forget what your code does in 6 months. Standardized, well-named code acts as its own documentation.

### Debugging
Properly formatted code makes logical errors "stand out." A missing space or a strange indentation level often signals where a bug is hiding.

---

## 5. Advantages & Disadvantages

### Advantages
- **Consistency**: The entire codebase looks like it was written by a single person.
- **Maintainability**: Easier to fix, update, and refactor.
- **Professionalism**: Signals to employers and auditors that you are a serious engineer.

### Disadvantages
- **Initial effort**: It takes more time to think of a good name than to type `x`.
- **Rigidity**: Some developers feel restricted by "strict" rules (though PEP 8 is fairly flexible).

---

## 6. Real-World Use Cases

### Case 1: FDA/Regulatory Compliance
Medical device software (Class II or III) requires extensive documentation. Using standard naming and structure is often part of the quality management system (QMS) requirements.

### Case 2: Open Source Contribution
If you want to contribute to professional Python libraries like `NumPy` or `Django`, your code *must* meet their style guidelines or it will be rejected.

---

## 7. Best Practices

### Best Practice 1: Names should tell a story
A variable should explain what it holds.
- **Bad**: `v = 15.5`
- **Good**: `glucose_level_mmol = 15.5`

### Best Practice 2: DRY (Don't Repeat Yourself)
If you are copy-pasting code, you are violating a standard. Wrap that logic in a well-named function.

### Best Practice 3: Use Linting Tools
Don't guess! Use tools like **Flake8**, **Pylint**, or **Black** to automatically check and format your code.

---

## 8. Top 3 Mistakes

### Mistake 1: Mixed Naming styles
#### Improper Code
```python
my_age = 25
PatientName = "John" # Mixing camelCase/PascalCase with snake_case
def CalcDose(): # Should be calc_dose
    pass
```

### Mistake 2: Magic Numbers
#### Improper Code
```python
# What does 0.45 represent?
weight_kg = weight_lbs * 0.45
```
#### Correction
```python
LBS_TO_KG_FACTOR = 0.453
weight_kg = weight_lbs * LBS_TO_KG_FACTOR
```

### Mistake 3: Commenting the Obvious
#### Improper Code
```python
x = x + 1 # Increment x by 1 (Completely useless comment)
```
#### Correction
```python
# Increase patient encounter count for billing threshold
visit_count += 1
```
