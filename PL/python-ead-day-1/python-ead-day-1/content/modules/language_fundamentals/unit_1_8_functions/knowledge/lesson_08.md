---
title: "Functions: Modular Coding Power"
type: knowledge
module: language_fundamentals
unit: unit_1_8_functions
order: 8
difficulty: beginner
tags:
  subtopics:
    - parameters
    - returns
    - scope
    - docstrings
---

# Unit 1.8: Functions

## 1. What
**Functions** are reusable blocks of code designed to perform a single, related action. They provide better modularity for your application and a high degree of code reuse.

In healthcare, functions are essential for ensuring that critical calculations (like drug dosages) are performed identically everywhere in the system. Instead of writing the "Dosage Formula" 10 times, you write it once as a function and call it 10 times.

---

## 2. Example

### Example 1: Basic Function with Return
```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Calling the function
current_bmi = calculate_bmi(70, 1.75)
print(f"Patient BMI: {current_bmi}")
```

### Example 2: Default Parameters
```python
def record_vitals(heart_rate, heart_rhythm="Regular"):
    """Logs patient vitals with a default rhythm."""
    print(f"Logging: HR {heart_rate} BPM, Rhythm: {heart_rhythm}")

record_vitals(72)                  # Uses default "Regular"
record_vitals(110, "Arrhythmic")   # Overrides default
```

### Example 3: Positional vs Keyword Arguments
```python
def create_patient(first_name, last_name, age):
    return f"{last_name}, {first_name} (Age: {age})"

# Positional (Order matters)
print(create_patient("John", "Doe", 45))

# Keyword (Order doesn't matter, extremely clear)
print(create_patient(age=45, last_name="Doe", first_name="John"))
```

---

## 3. Explanation

### Anatomy of a Function
1.  **Keyword `def`**: Signals the start of a function definition.
2.  **Name**: Follows the same rules as variables (lowercase_with_underscores).
3.  **Parameters**: Inputs listed inside parentheses.
4.  **Body**: Indented block of code.
5.  **Return Statement**: Sends a value back to where the function was called. Use `return` to exit the function early.

### Local vs Global Scope
- **Local Scope**: Variables created *inside* a function. They only exist while the function is running.
- **Global Scope**: Variables created *outside* any function. They are accessible everywhere, but modifying them inside a function requires the `global` keyword (which is usually discouraged).

---

## 4. Why

### Don't Repeat Yourself (DRY)
Functions eliminate redundancy. If you need to change a logic rule (e.g., updating a safety threshold), you only change it in one place.

### Readability
Well-named functions act as documentation. Reading `admit_patient(p_id)` is much clearer than reading 20 lines of database and logic code.

### Testing
It is much easier to test a 5-line function that calculates a score than to test a 500-line script that does everything.

---

## 5. Advantages & Disadvantages

### Advantages
- **Abstraction**: You don't need to know *how* a function works to use it.
- **Namespace isolation**: Variables inside a function won't accidentally overwrite variables outside.
- **Organization**: Allows complex problems to be broken into manageable chunks.

### Disadvantages
- **Overhead**: Function calls have a tiny performance cost (unnoticeable in most Python apps).
- **Misuse**: "Hard-to-read" functions that do too many things can actually make code worse.

---

## 6. Real-World Use Cases

### Case 1: Triage Logic Wrapper
Wrapping complex if/else trees into a single, testable call.
```python
def get_triage_color(bp_systolic):
    if bp_systolic > 180: return "Red"
    if bp_systolic > 140: return "Yellow"
    return "Green"
```

### Case 2: Conversion Utilities
Standardizing units throughout a clinical application.
```python
def lbs_to_kg(weight_lbs):
    return weight_lbs * 0.453592
```

---

## 7. Best Practices

### Best Practice 1: Single Responsibility
A function should do **one thing well**. If you find yourself naming a function `calculate_and_save_and_print()`, it should probably be three separate functions.

### Best Practice 2: Use Docstrings
Always document what your function does, especially the units of any numeric inputs.
```python
def calc_dose(weight_kg):
    """
    Args: weight_kg (float): Patient weight in kg.
    Returns: float: Dose in mg.
    """
    return weight_kg * 10
```

### Best Practice 3: Immutable Defaults
Avoid using mutable objects (like lists or dicts) as default parameter values.
```python
# Bad
def add_note(note, history=[]): ...

# Good
def add_note(note, history=None):
    if history is None:
        history = []
```

---

## 8. Top 3 Mistakes

### Mistake 1: Forgetting to `return`
#### Improper Code
```python
def add(a, b):
    res = a + b
    # Missing return!
    
val = add(5, 5) # val is now None
```

### Mistake 2: Shadowing Built-in names
#### Improper Code
```python
def min(x, y): # This overwrites the built-in min() function
    return x if x < y else y
```

### Mistake 3: Modification of Global State
#### Improper Code
```python
total_patients = 0

def add_patient():
    total_patients += 1 # ERROR: Cannot modify global without 'global' keyword
```
#### Correction
Pass the count in and return the new count, or use a class (covered in later modules).
