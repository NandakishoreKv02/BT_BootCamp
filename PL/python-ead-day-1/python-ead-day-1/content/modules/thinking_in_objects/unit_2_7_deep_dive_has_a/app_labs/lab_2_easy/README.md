---
title: "The Nursing Station Association"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 2
difficulty: easy
use_case: one-to-many-aggregation
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["aggregation", "multiplicity", "one-to-many"]
---

# Lab 2: The Nursing Station Association

**Module**: Thinking in Objects
**Objective**: Implement a **One-to-Many Aggregation** relationship where a station manages a group of nurses who exist independently.
**Difficulty**: Easy
**Context**: Ward Coordination

## Problem Statement
A `NursingStation` is responsible for coordinating several `Nurse` objects. Unlike beds in a ward, nurses aren't "part" of the station's structure—they are professionals assigned to it. If the station closes, the nurses still exist.

## Requirements
1.  **Modeling (Aggregation)**:
    - `Nurse` class with a `name`.
    - `NursingStation` class with an `id` and an empty list of `nurses`.
2.  **Implementation**:
    - Add a method `assign_nurse(self, nurse_obj)` to the station.
3.  **Validation**:
    - Create two nurses, create a station, and assign both nurses to it.

## Expected Output
```text
Station 5A established.
Nurses assigned: ['Nightingale', 'Barton']
```
