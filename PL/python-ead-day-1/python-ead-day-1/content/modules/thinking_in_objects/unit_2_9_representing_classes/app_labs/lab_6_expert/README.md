---
title: "The Department Hierarchist"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 6
difficulty: expert
use_case: complex-instantiation-hierarchy
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["instantiation", "logic-in-constructor", "pep-8"]
---

# Lab 6: The Department Hierarchist

**Module**: Thinking in Objects
**Objective**: Build a class that manages complex initialization logic and internal object references.
**Difficulty**: Expert
**Context**: Hospital Structural Management

## Problem Statement
A `HospitalDepartment` is a complex entity. When created, it must:
1.  Store its name and floor number.
2.  Determine its "Urgency Level" based on its name (e.g., "ER" and "ICU" are "High", all others are "Normal").
3.  Support sub-units (other instances of the same class) added via a method.

## Requirements
1.  **Strict Standards**:
    - Complete PEP 8 compliance.
2.  **Logic-in-Constructor**:
    - The `urgency` attribute should NOT be an argument in `__init__`. It must be calculated automatically from the `name`.
3.  **Hierarchy**:
    - Implement `add_subunit(self, dept_obj)`.
4.  **Reporting**:
    - A method to print the department and its sub-units.

## Expected Output
```text
Dept: Emergency [Urgency: High]
  - Subunit: Triage [Urgency: Normal]
  - Subunit: Trauma 1 [Urgency: Normal]
```
