---
title: "The Dosage Safety Gate"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 3
difficulty: intermediate
use_case: property-setter-validation
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["setter", "validation", "data-integrity"]
---

# Lab 3: The Dosage Safety Gate

**Module**: Thinking in Objects
**Objective**: Implement clinical validation logic using a `@property.setter`.
**Difficulty**: Intermediate
**Context**: Pharmacy Automation

## Problem Statement
A `MedicationRequest` object tracks the `dosage` in milligrams (mg). For patient safety, the dosage must never be negative and must never exceed a maximum safety limit (e.g., 500mg).

## Requirements
1.  **Modeling**:
    - Class `MedicationRequest`.
2.  **Encapsulation**:
    - Manage dosage via a `@property`.
    - Implement a `.setter` that checks: `0 < value <= 500`.
3.  **Sanatization**:
    - If the value is invalid, print a warning and DO NOT update the internal attribute.

## Expected Output
```text
Setting dose to 250mg... Success.
Setting dose to 999mg... Error: Safety limit exceeded!
Current Dose: 250mg
```
