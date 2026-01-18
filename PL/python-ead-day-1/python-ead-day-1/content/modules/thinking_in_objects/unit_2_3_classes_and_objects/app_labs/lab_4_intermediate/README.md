---
title: "The Virtual Ward"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 4
difficulty: intermediate
use_case: collection-of-objects
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["collections", "composition-basics", "methods"]
---

# Lab 4: The Virtual Ward

**Module**: Thinking in Objects
**Objective**: manage multiple objects of the same class by storing them in a "Container" (Ward) and interacting with them through instance methods.
**Difficulty**: Intermediate
**Context**: Hospital Staffing

## Problem Statement
A ward needs to track multiple doctors. We want a `Ward` class that can "admit" `Doctor` objects and perform analysis on the entire group (e.g., counting a specific specialty).

## Requirements
1.  **Doctor Class**: `__init__(self, name, specialty)`.
2.  **Ward Class**:
    - `__init__(self, ward_name)`: Stores an empty list `doctors`.
    - `add_doctor(self, doctor_obj)`: Adds the object to the list.
    - `get_census(self)`: Returns a string describing the ward.
3.  **Cross-Object Interaction**: In `main`, create doctors and "assign" them to a ward.

## Expected Output
```text
Ward: Cardiology Unit
Staff Census: 2 Doctors
- Dr. Smith (Cardio)
- Dr. Jones (Cardio)
```
