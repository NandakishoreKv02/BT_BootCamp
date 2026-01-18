# Lab 6 Tasks: Duplicate vs Unique Patients

## Task 1: Prove Object Identity
**Difficulty**: Advanced | **Points**: 100

### Objective
Understand memory references.

### Requirements
- Create a `Patient` class.
- Create two instances: `patient_a` and `patient_b`, both with the name "John".
- Prove that `patient_a is patient_b` is `False`.
- Create a third variable `alias_a` and set it to `patient_a`.
- Prove that `alias_a is patient_a` is `True`.
