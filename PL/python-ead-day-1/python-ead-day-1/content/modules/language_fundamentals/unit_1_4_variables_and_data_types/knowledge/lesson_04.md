---
title: "Variables & Data Types: Storing and Manipulating Information"
type: knowledge
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
order: 4
difficulty: beginner
tags:
  subtopics:
    - variables
    - primitive-types
    - type-casting
    - mutability
    - pep8
---

# Unit 1.4: Variables & Data Types

## 1. What
In programming, **variables** are named containers for storing data values. Unlike some languages where you must declare a specific type (like `int x = 5;` in C++), Python is **dynamically typed**, meaning you don't need to declare the type, and a variable can change types during execution.

Python's core primitive data types include:
- **`int`**: Integers (whole numbers, e.g., `42`, `-5`)
- **`float`**: Floating-point numbers (decimals, e.g., `98.6`, `3.14`)
- **`str`**: Strings (text sequences, e.g., `"Patient Name"`)
- **`bool`**: Booleans (logic values, `True` or `False`)

Python also enforces **strong typing** (you can't just add a string to a number) and has strict rules about **mutability** (whether an object can be changed after creation).

---

## 2. Example

### Example 1: Defining Variables and Types
```python
# 1. Integer (int) - Whole numbers
patient_age = 45
heart_rate = 72

# 2. Float (float) - Decimals
body_temperature = 37.5
weight_kg = 75.4

# 3. String (str) - Text
patient_name = "John Doe"
blood_type = 'O+'

# 4. Boolean (bool) - True/False
is_admitted = True
has_insurance = False

# Inspecting types
print(type(patient_age))       # <class 'int'>
print(type(body_temperature))  # <class 'float'>
```

### Example 2: Dynamic Typing
```python
# A variable can hold different types over time (though not recommended practice)
status = "Active"       # Starts as string
print(type(status))     # <class 'str'>

status = 1              # Now it's an integer code
print(type(status))     # <class 'int'>

status = True           # Now it's a boolean
print(type(status))     # <class 'bool'>
```

### Example 3: Type Casting (Conversion)
```python
# Converting String to Int
age_input = "25"
age_int = int(age_input)  # Becomes integer 25

# Converting Float to Int (truncates decimal)
temp = 37.9
temp_int = int(temp)      # Becomes 37

# Converting Int/Float to String
id_number = 12345
id_str = str(id_number)   # Becomes "12345"

# Converting to Boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool("Hi"))     # True
print(bool(""))       # False (empty string is falsy)
```

### Example 4: Mutability vs Immutability
```python
# Strings are IMMUTABLE (Cannot change in place)
name = "Alice"
# name[0] = "B"   # ERROR: TypeError: 'str' object does not support item assignment

# Instead, you create a NEW string:
name = "B" + name[1:]  # Creates "Blice" (new object)

# Numbers are IMMUTABLE
count = 10
# When you do count += 1, you aren't changing the number 10,
# you are recalculating 10+1=11 and pointing 'count' to the new number 11.
```

---

## 3. Explanation

### Dynamic Typing
In Python, variables are essentially **labels** or tags attached to objects in memory.
- `x = 5`: Python creates an integer object `5` and puts a tag `x` on it.
- `x = "Hello"`: Python creates a string object `"Hello"` and moves the tag `x` to it. The `5` is eventually cleaned up by the garbage collector if no one else needs it.

### Variable Naming (PEP 8)
- **Functions & Variables**: Use `snake_case` (lowercase with underscores).
  - Good: `patient_id`, `calculate_bmi`, `is_active`
  - Bad: `PatientId`, `calculateBMI`, `IsActive`
- **Constants**: Use `UPPER_CASE` (underscores between words).
  - Good: `MAX_HEART_RATE`, `DEFAULT_TIMEOUT`
- **Classes**: Use `PascalCase` (Capitalize first letter of each word).
  - Good: `PatientRecord`, `HospitalDepartment`

### Type Checking
- **`type(obj)`**: Returns the exact type of the object.
- **`isinstance(obj, class)`**: Returns `True` if the object is an instance of the class (or subclass). **Preferred** for checking types because it respects inheritance.
  ```python
  if isinstance(val, (int, float)):  # Checks if it's a number
      print("Valid number")
  ```

### Mutability
- **Immutable Types**: `int`, `float`, `bool`, `str`, `tuple`.
  - Once created, their content cannot change. Any "change" creates a new object.
  - Safe to use as dictionary keys.
- **Mutable Types**: `list`, `dict`, `set`, `bytearray`.
  - Content can be modified in place without creating a new object.
  - Efficient for large collections but require care in multi-threaded apps.

---

## 4. Why

### Why Dynamic Typing?
- **Flexibility**: Reduces boilerplate code. No need to write `int`, `String` everywhere.
- **Speed of Development**: You can prototype faster.
- **Polymorphism**: Functions can naturally handle different data types if they support the same operations (Duck Typing).

### Why Strict Naming Conventions?
- **Readability**: Code is read more often than it is written.
- **Consistency**: In large teams (or open source), everyone knows that `Patient` is likely a class and `patient` is an instance, just by looking at the name.

### Why Immutability Matters in Healthcare?
- **Data Integrity**: If you pass a patient's ID string to a function, you want to be 100% sure that function cannot accidentally modify the ID in place.
- **Concurrency**: Immutable objects are thread-safe by default (no need for locks since they can't change).

---

## 5. Advantages & Disadvantages

### Advantages
- **Ease of Use**: No need for verbose type declarations.
- **Powerful String Handling**: Python's `str` type is extremely powerful and works with Unicode out of the box (critical for international patient names).
- **Safety**: Strong typing prevents logical errors like `1 + "2"` which happens in JavaScript (producing `"12"`).

### Disadvantages
- **Runtime Errors**: Type errors (like `TypeError`) happen when the code *runs*, not when it compiles.
- **Performance**: Dynamic typing requires Python to check types at runtime, making it slower than C/C++.
- **Memory Overhead**: Every integer in Python is an object, taking more memory than a raw C integer.

---

## 6. Real-World Use Cases

### Case 1: Calculating BMI (Float & Casting)
```python
weight_input = "70.5"  # From a form (string)
height_input = "1.75"

# Must cast to float before math
weight = float(weight_input)
height = float(height_input)

bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")  # Formatting float to 2 decimals
```

### Case 2: Patient Triage Flag (Boolean Logic)
```python
heart_rate = 110
spo2 = 92

# Boolean expression
is_critical = (heart_rate > 100) and (spo2 < 95)

if is_critical:
    print("Code Red: Immediate Attention Required")
```

### Case 3: Generating HL7 Messages (String Manipulation)
```python
pid = 12345
name = "Smith^John"
dob = "19800101"

# Using integers and strings together
# Casting int to str for concatenation
message = "PID|1|" + str(pid) + "||" + name + "||" + dob
print(message)
# Output: PID|1|12345||Smith^John||19800101
```

---

## 7. Best Practices

### Best Practice 1: Use Snake Case for Variables
**Why**: It's the community standard.
```python
# Good
patient_dob = "1990-05-20"

# Bad
patientDOB = "1990-05-20"
PatientDob = "1990-05-20"
```

### Best Practice 2: Verify Input Types Early
**Why**: Prevent crashing later in the logic.
```python
def calculate_dosage(weight_kg):
    if not isinstance(weight_kg, (int, float)):
        raise TypeError("Weight must be a number")
    # ... calculation
```

### Best Practice 3: Avoid "Magic Numbers"
**Why**: Code becomes unreadable. Use constant variables instead.
```python
# Bad
if heart_rate > 100: ...

# Good
TACHYCARDIA_THRESHOLD = 100

if heart_rate > TACHYCARDIA_THRESHOLD: ...
```

---

## 8. Top 3 Mistakes

### Mistake 1: Comparing Incompatible Types
#### Improper Code
```python
age = 25
age_input = "25"

if age == age_input:  # Always False! 25 != "25"
    print("Match")
```
#### Correction
```python
if str(age) == age_input:
    print("Match")
```

### Mistake 2: Assuming Float Precision
#### Improper Code
```python
val = 0.1 + 0.2
if val == 0.3:  # False! val is actually 0.30000000000000004
    print("Equal")
```
#### Correction
```python
import math
if math.isclose(val, 0.3):
    print("Equal")
```

### Mistake 3: Misunderstanding Variable Assignment
#### Improper Code
```python
a = 5
b = a  # b points to 5
a = 10 # a now points to 10

# Beginner assumes b also changed to 10
# But b is still 5
```
**Fix**: Understand that variables are references. Assigning a new value to `a` just moves the tag; it doesn't affect `b` unless `b` is mutable (list/dict) and you modified the content in place.
