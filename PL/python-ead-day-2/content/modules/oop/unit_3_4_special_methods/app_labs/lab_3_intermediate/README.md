---
title: "Medical Record System - Priority Queue"
type: app_lab
module: oop
unit: unit_3_4_special_methods
lab_number: 3
difficulty: intermediate
use_case: medical_record_system
domain: healthcare
order: 3
duration_hours: 2.5
tags:
  topics: ["oop", "special-methods", "comparison"]
  subtopics:
    - eq-method
    - lt-method
    - sorting
---

# Lab 3: Medical Record System - Priority Queue

**Objective**: Implement comparison methods for patient triage
**Difficulty**: Intermediate

## Use Case

Emergency room patients need to be prioritized. Create a TriagePatient class that can be compared and sorted by urgency level.

## Task Summary

- **Task 1**: Create TriagePatient with urgency level (1=critical, 5=minor)
- **Task 2**: Implement `__eq__` for patient ID comparison
- **Task 3**: Implement `__lt__` for urgency-based sorting
- **Task 4**: Use `@total_ordering` for complete comparisons
- **Task 5**: Test sorting a list of patients
