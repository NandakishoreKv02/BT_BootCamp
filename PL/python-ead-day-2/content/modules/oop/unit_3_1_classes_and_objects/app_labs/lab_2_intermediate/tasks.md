# Lab 2 Tasks: Clinical Vitals Tracker

## Task 1: Initialize the Vitals List
**Difficulty**: Easy | **Points**: 20

### Objective
Prepare the object to store multiple readings.

### Requirements
- Update the `Patient` `__init__` method.
- Initialize an instance variable named `self.vitals` as an empty list `[]`.
- It should NOT be passed as a parameter; every new patient starts with an empty history.

---

## Task 2: Implement add_vital() Method
**Difficulty**: Intermediate | **Points**: 35

### Objective
Create a way to update the patient's record.

### Requirements
- Create an instance method `add_vital(self, heart_rate)`.
- Append the `heart_rate` value to the `self.vitals` list.
- Print a confirmation message: "Heart rate [val] recorded for [name]".

---

## Task 3: Implement get_average_heart_rate() Method
**Difficulty**: Intermediate | **Points**: 45

### Objective
Perform data analysis on instance state.

### Requirements
- Create an instance method `get_average_heart_rate(self)`.
- Calculate the average of all numbers in `self.vitals`.
- **Constraint**: If `self.vitals` is empty, return `0.0` to avoid a division by zero error.
- Return the numeric average.

### Example
```python
p = Patient("P1", "Alice", 25)
p.add_vital(100)
p.add_vital(50)
print(p.get_average_heart_rate()) # Expected: 75.0
```
