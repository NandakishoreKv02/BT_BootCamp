---
title: "The Nursing Shift Network"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 5
difficulty: advanced
use_case: many-to-many-aggregation
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["many-to-many", "aggregation", "sync"]
---

# Lab 5: The Nursing Shift Network

**Module**: Thinking in Objects
**Objective**: Implement a **Many-to-Many Aggregation** relationship where nurses work across multiple departments and departments manage multiple nurses.
**Difficulty**: Advanced
**Context**: Workforce Management

## Problem Statement
In a flexible hospital environment, a `Nurse` can be assigned to multiple `Department` objects during a week. Simultaneously, a `Department` has a rotation of many `Nurse` objects. 

Your task is to model this M:N relationship, ensuring that when a nurse is assigned to a department, both objects update their internal records.

## Requirements
1.  **Modeling (M:N)**:
    - `Nurse` (list of departments).
    - `Department` (list of nurses).
2.  **Double-Sync Logic**:
    - Method `assign_to_department(self, dept_obj)` in the `Nurse` class.
    - It should add the department to the nurse's list AND add the nurse to the department's list.
3.  **Safety**:
    - Ensure that duplicate assignments are prevented (e.g., don't add the same nurse twice to the same department).

## Expected Output
```text
Assigning Nurse Joy to Cardiac...
Assigning Nurse Joy to ICU...
Joy's Schedule: ['Cardiac', 'ICU']
ICU Staff: ['Joy']
```
