# Lab 1 Tasks: Clinic Admission Portal

## Task 1: Initialize the Patient State
**Difficulty**: Easy | **Points**: 20

### Objective
Define the initial data for a patient.

### Requirements
- Create a `Patient` class.
- The `__init__` method should accept `name`.
- Initialize `self.name` with the input.
- Initialize `self.is_active` as `False`.

---

## Task 2: Implement 'admit()' Method
**Difficulty**: Easy | **Points**: 40

### Objective
Change an object's state to "admitted".

### Requirements
- Create an instance method `admit(self)`.
- Set `self.is_active` to `True`.
- Return the string: "Patient [name] successfully admitted."

---

## Task 3: Implement 'discharge()' Method
**Difficulty**: Easy | **Points**: 40

### Objective
Change an object's state to "discharged".

### Requirements
- Create an instance method `discharge(self)`.
- Set `self.is_active` to `False`.
- Return the string: "Patient [name] successfully discharged."
