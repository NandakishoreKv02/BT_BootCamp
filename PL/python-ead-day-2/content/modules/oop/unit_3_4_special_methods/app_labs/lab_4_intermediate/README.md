---
title: "Medical Record System - Diagnosis Codes"
type: app_lab
module: oop
unit: unit_3_4_special_methods
lab_number: 4
difficulty: intermediate
use_case: medical_record_system
domain: healthcare
order: 4
duration_hours: 2.5
tags:
  topics: ["oop", "special-methods", "hashing"]
  subtopics:
    - eq-method
    - hash-method
    - set-operations
---

# Lab 4: Medical Record System - Diagnosis Codes

**Objective**: Implement `__eq__` and `__hash__` for hashable medical codes
**Difficulty**: Intermediate

## Use Case

Medical diagnosis codes (like ICD-10) need to be stored in sets and used as dictionary keys. Create a DiagnosisCode class that is hashable.

## Task Summary

- **Task 1**: Create DiagnosisCode with code and description
- **Task 2**: Implement `__eq__` based on code
- **Task 3**: Implement `__hash__` based on code
- **Task 4**: Test usage in sets and dicts
- **Task 5**: Verify duplicate handling
