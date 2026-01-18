---
title: "The Global Bed Manager"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 1
difficulty: easy
use_case: refactoring
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["scope", "dictionaries", "refactoring"]
---

# Lab 1: The Global Bed Manager

**Module**: Thinking in Objects
**Objective**: Refactor a script that uses global variables to manage hospital beds into a dictionary-based "Ward Object". 
**Difficulty**: Easy
**Context**: Hospital Capacity Management

## Problem Statement
The current code uses global variables `total_beds` and `occupied_beds`. This means the software can only manage **one single ward** for the entire hospital. This is a perfect example of why global state limits scalability.

Your job is to refactor this so we can create multiple independent Wards (e.g., "ICU", "General", "Pediatrics").

## Requirements
1.  **Remove Globals**: Eliminate `global` keywords.
2.  **Constructor**: Create `make_ward(name, total_beds)` that returns a dictionary: `{'name': ..., 'total': ..., 'occupied': 0}`.
3.  **Methods**: 
    - `admit_patient(ward_dict)`: Increases occupancy if space exists.
    - `discharge_patient(ward_dict)`: Decreases occupancy if not empty.
    - `get_status(ward_dict)`: Returns a formatted string.

## Expected Output
```text
ICU: 1/10 beds occupied
General: 5/20 beds occupied
```
(Notice how the two wards operate independently?)
