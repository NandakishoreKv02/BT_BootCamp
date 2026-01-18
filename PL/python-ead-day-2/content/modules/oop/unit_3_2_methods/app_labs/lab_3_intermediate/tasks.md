# Lab 3 Tasks: Clinic-Wide Census tracking

## Task 1: Add a Class Variable
**Difficulty**: Easy | **Points**: 20

### Objective
Store data at the class level.

### Requirements
- Update the `Patient` class.
- Add a class variable `census = 0`.
- This variable must be shared by all instances.

---

## Task 2: Track Admission and Discharge
**Difficulty**: Intermediate | **Points**: 45

### Objective
Update shared state from instance methods.

### Requirements
- In `__init__`, increment `Patient.census` by 1.
- Implement an instance method `discharge(self)`.
- In `discharge()`, decrement `Patient.census` by 1 **only if** the census is greater than 0.

---

## Task 3: Implement '@classmethod get_census'
**Difficulty**: Intermediate | **Points**: 35

### Objective
Retrieve shared state via class-level interface.

### Requirements
- Create a `@classmethod` named `get_census(cls)`.
- It should return the current value of the class variable.

### Example
```python
p1 = Patient("Alice")
p2 = Patient("Bob")
print(Patient.get_census()) # Expected: 2
p1.discharge()
print(Patient.get_census()) # Expected: 1
```
