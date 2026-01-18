# Lab 4 Tasks: Smart Patient registration

## Task 1: Implement 'from_string' Factory
**Difficulty**: Intermediate | **Points**: 50

### Objective
Create an alternative constructor for formatted text data.

### Requirements
- Create a `@classmethod` named `from_string(cls, data_str)`.
- Input format: `"Name-Age"`.
- Split the string, convert age to int, and return a new instance.

---

## Task 2: Implement 'from_dict' Factory
**Difficulty**: Intermediate | **Points**: 50

### Objective
Create an alternative constructor for structured data.

### Requirements
- Create a `@classmethod` named `from_dict(cls, data_dict)`.
- Expected keys: `"name"` and `"age"`.
- Return a new instance using data from the dictionary.

### Example
```python
p = Patient.from_string("Alice-30")
p2 = Patient.from_dict({"name": "Bob", "age": 45})
```
