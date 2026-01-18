---
title: "The Multi-Sourced Patient Portal"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 6
difficulty: expert
use_case: complex-state-validation-constructor
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["initialization", "validation", "logic-abstraction", "constructor"]
---

# Lab 6: The Multi-Sourced Patient Portal

**Module**: Thinking in Objects
**Objective**: Build a constructor that performs complex cross-parameter validation to ensure object integrity.
**Difficulty**: Expert
**Context**: Clinical Data Integration

## Problem Statement
A `PatientProfile` is initialized with a `data_source` (e.g., "EHR", "Manual", "Legacy"). 
- If the source is "EHR", an `ehr_id` MUST be provided.
- If the source is "Manual", the `ehr_id` should default to `None`.
- The constructor should validate this relationship. If an "EHR" source is provided without an ID, the constructor should raise a `ValueError`.

## Requirements
1.  **Architecture**:
    - Class `PatientProfile`.
2.  **Strict Validation**:
    - Constructor must check the relationship between `data_source` and `ehr_id`.
3.  **Encapsulation**:
    - Use properties to expose the data, keeping the raw initialization logic protected in the constructor.

## Expected Output
```text
Manual Profile Created: Bob
EHR Profile Created: Alice (ID: 999)
ERROR: EHR source requires an ID!
```
