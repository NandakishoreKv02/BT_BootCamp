---
title: "Medical Record System - Patient Registry"
type: app_lab
module: oop
unit: unit_3_4_special_methods
lab_number: 2
difficulty: easy
use_case: medical_record_system
domain: healthcare
order: 2
duration_hours: 2
tags:
  topics: ["oop", "special-methods", "collections"]
  subtopics:
    - len-method
    - getitem-method
    - contains-method
---

# Lab 2: Medical Record System - Patient Registry

**Objective**: Implement `__len__`, `__getitem__`, and `__contains__` for a patient registry
**Difficulty**: Easy

## Use Case

Create a PatientRegistry class that behaves like a collection, allowing:
- `len(registry)` to get patient count
- `registry["P001"]` to get patient by ID
- `"P001" in registry` to check existence

## Task Summary

- **Task 1**: Create PatientRegistry with internal storage
- **Task 2**: Implement `__len__` method
- **Task 3**: Implement `__getitem__` for ID lookup
- **Task 4**: Implement `__contains__` for membership testing
