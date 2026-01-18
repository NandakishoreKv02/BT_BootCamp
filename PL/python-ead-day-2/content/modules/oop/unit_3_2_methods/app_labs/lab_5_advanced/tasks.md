# Lab 5 Tasks: Clinical Utility Suite

## Task 1: Logic Separation
**Difficulty**: Intermediate | **Points**: 30

### Objective
Identify logic that belongs in a static method.

### Requirements
- Create a `@staticmethod` named `calculate_bmi(weight_kg, height_m)`.
- Use the formula: `weight / (height * height)`.

---

## Task 2: Height Zero Protection
**Difficulty**: Advanced | **Points**: 40

### Objective
Implement error handling in utilities.

### Requirements
- Update `calculate_bmi`.
- If `height_m` is 0, return `0.0`.
- Otherwise, return the calculated BMI rounded to 2 decimal places.

---

## Task 3: Practical Integration
**Difficulty**: Advanced | **Points**: 30

### Objective
Use a static method within an instance method.

### Requirements
- Create an instance method `get_my_bmi(self)`.
- Assume the object has `self.weight` and `self.height`.
- Call the static method and return the result.
