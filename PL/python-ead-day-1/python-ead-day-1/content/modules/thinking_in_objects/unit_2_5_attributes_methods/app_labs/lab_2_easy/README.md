---
title: "The Hospital Census Tracker"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 2
difficulty: easy
use_case: class-attributes
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["attributes", "state", "class-level"]
---

# Lab 2: The Hospital Census Tracker

**Module**: Thinking in Objects
**Objective**: implement **Class Attributes** to track institutional-level data shared across all objects.
**Difficulty**: Easy
**Context**: Hospital Administration

## Problem Statement
Every time a patient is admitted, the hospital's total census (count) increases. While each `Admission` object is unique, the `total_admissions` count belongs to the entire hospital system.

Your task is to use a **Class Attribute** to track the total number of patients admitted during the program's execution.

## Requirements
1.  **Shared State**:
    - Use a class attribute `census` initialized to 0.
2.  **Implementation**:
    - In the `__init__` method, increment the class attribute.
3.  **Validation**:
    - Create 5 admission objects and print the final census from the class itself (not an instance).

## Expected Output
```text
Admitting Patient A...
Admitting Patient B...
TOTAL HOSPITAL CENSUS: 2
```
