# Lab 3 Tasks: Hospital Ward Manager

## Task 1: Global Occupancy Tracking
**Difficulty**: Intermediate | **Points**: 20

### Objective
Manage shared hospital state.

### Requirements
- Add a class variable `total_patients = 0` to the `Patient` class.
- Update `__init__` to increment this variable every time a new patient is created.
- Create a `@classmethod` named `get_census(cls)` that returns the current `total_patients`.

---

## Task 2: Advanced Treatment Logic
**Difficulty**: Advanced | **Points**: 40

### Objective
Handle side effects and return values.

### Requirements
- Implement an instance method `prescribe_medication(self, med_name, dosage_mg)`.
- It should:
  1. Add a dictionary `{"med": med_name, "dose": dosage_mg}` to an instance list `self.records`.
  2. Increment `self.treatment_count`.
  3. Return a string: "Prescribed [dose]mg of [med] to [name]".
- This method has **both** side effects (updating state) and a return value.

---

## Task 3: Static Utility Integration
**Difficulty**: Advanced | **Points**: 20

### Objective
Modularize logic.

### Requirements
- Create a `@staticmethod` named `calculate_risk_score(age, weight)`.
- Logic: `(age * 0.5) + (weight * 0.2)`.
- Integrate this: Create an instance method `get_priority(self)` that calls the static method using its own `age` and `weight` and returns the score.

---

## Task 4: Safe Discharge
**Difficulty**: Advanced | **Points**: 20

### Objective
System safety.

### Requirements
- Implement an instance method `discharge(self)`.
- It should:
  1. Decrement the class variable `total_patients`.
  2. Set an instance variable `self.active = False`.
  3. **Constraint**: Ensure the global count doesn't go below zero.
  4. Return `True` on success.

### Example
```python
p1 = Patient("Alice", 30, 60) # total_patients = 1
p1.prescribe_medication("Advil", 200)
print(p1.get_priority()) # Calling static method via instance
p1.discharge() # total_patients = 0
```
