# Lab 2 Tasks: Real-time Vitals Update

## Task 1: Initialize Vitals
**Difficulty**: Easy | **Points**: 20

### Objective
Store numeric health data.

### Requirements
- Update the `Patient` constructor to accept `name`.
- Initialize `self.temperature` to `0.0`.
- Initialize `self.heart_rate` to `0`.

---

## Task 2: Implement 'update_temperature()'
**Difficulty**: Easy | **Points**: 40

### Objective
Safely update decimal values.

### Requirements
- Create a method `update_temperature(self, celsius)`.
- **Validation**: Only update if `30.0 <= celsius <= 45.0`.
- Return `True` if updated, `False` otherwise.

---

## Task 3: Implement 'update_heart_rate()'
**Difficulty**: Easy | **Points**: 40

### Objective
Safely update integer values.

### Requirements
- Create a method `update_heart_rate(self, bpm)`.
- **Validation**: Only update if `0 < bpm < 300`.
- Return `True` if updated, `False` otherwise.
