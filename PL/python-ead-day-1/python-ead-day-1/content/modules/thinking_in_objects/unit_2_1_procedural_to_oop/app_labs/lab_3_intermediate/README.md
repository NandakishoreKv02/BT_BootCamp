---
title: "Breaking the Triage Monolith"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 3
difficulty: intermediate
use_case: refactoring
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["functions", "refactoring", "context-object"]
---

# Lab 3: Breaking the Triage Monolith

**Module**: Thinking in Objects
**Objective**: Break down a monolithic "God Function" (handles admission, vitals check, and priority assignment) into specialized functions operating on a Patient Object.
**Difficulty**: Intermediate
**Context**: ER Triage

## Problem Statement
The starter code has `process_patient_entry` which does everything.
1. Validates age.
2. Checks vitals.
3. Assigns priority.
4. Prints a wristband.

This is fragile. We want a pipeline of small functions.

## Requirements
1.  **Create Context**: `create_triage_record(name, age, heart_rate, complaint)` returns a dict.
2.  **Specialized Functions**:
    - `validate_age(record)`
    - `assess_severity(record)` (Sets priority based on HR/complaint)
    - `print_wristband(record)`
3.  **No Globals**: The record dictionary carries state through the pipeline.

## Expected Output
```text
Wristband: [John Doe] - Priority: HIGH
```
