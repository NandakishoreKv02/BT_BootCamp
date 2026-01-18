# Lab 2 Tasks: Smart Patient Intake

## Task 1: Basic Constructor
**Difficulty**: Easy | **Points**: 10

### Objective
Define the base state.

### Description
Create a `Patient` class. The `__init__(self, name, age, condition)` method should assign these three parameters to instance variables.

---

## Task 2: Implement 'from_string' Factory
**Difficulty**: Intermediate | **Points**: 45

### Objective
Parse legacy data formats.

### Requirements
- Create a `@classmethod` named `from_string(cls, data_str)`.
- Input format: `"Name:Age:Condition"`.
- Action:
  1. Split the string by `:`.
  2. Convert age to an integer.
  3. Return a new instance using `cls(name, age, condition)`.

---

## Task 3: Implement 'from_dict' Factory
**Difficulty**: Intermediate | **Points**: 45

### Objective
Handle modern structured data.

### Requirements
- Create a `@classmethod` named `from_dict(cls, data_dict)`.
- Action:
  1. Extract `name`, `age`, and `condition` from the dictionary.
  2. Return a new instance using `cls(...)`.
  3. Hint: Use `data_dict.get('key')` for safety.

### Example
```python
p = Patient.from_string("Sarah:28:Allergy")
print(p.name) # Expected: Sarah

p2 = Patient.from_dict({"name": "Tom", "age": 40, "condition": "None"})
print(p2.age) # Expected: 40
```
