---
title: "Medical Record System - Validation Engine"
type: app_lab
module: oop
unit: unit_3_4_special_methods
lab_number: 5
difficulty: advanced
use_case: medical_record_system
domain: healthcare
order: 5
duration_hours: 3
tags:
  topics: ["oop", "special-methods", "callable"]
  subtopics:
    - call-method
    - validators
    - functional-objects
---

# Lab 5: Medical Record System - Validation Engine

**Objective**: Implement `__call__` for callable validator objects
**Difficulty**: Advanced

## Use Case

Medical data needs validation before storage. Create callable validator classes that can be used like functions but maintain state and configuration.

## Task Summary

- **Task 1**: Create RangeValidator with min/max bounds
- **Task 2**: Implement `__call__` to validate values
- **Task 3**: Create PatternValidator for format checking
- **Task 4**: Build ValidatorChain combining multiple validators
- **Task 5**: Apply to vital signs validation
- **Task 6**: Handle validation errors with messages
