---
title: "The Multi-Bed Ward"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 1
difficulty: easy
use_case: one-to-many-composition
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["composition", "multiplicity", "one-to-many"]
---

# Lab 1: The Multi-Bed Ward

**Module**: Thinking in Objects
**Objective**: Implement a **One-to-Many Composition** relationship to model a hospital ward that contains multiple beds.
**Difficulty**: Easy
**Context**: Inpatient Ward Management

## Problem Statement
A `HospitalWard` is a structural entity that contains and owns multiple `Bed` objects. When a ward is initialized, it should automatically create a specified number of beds.

## Requirements
1.  **Modeling (1:N)**:
    - `Bed` class with a `bed_number`.
    - `HospitalWard` class with a `name` and a list of beds.
2.  **Implementation**:
    - In `HospitalWard.__init__`, use a loop to populate the `beds` list with new `Bed` objects.
3.  **Validation**:
    - Create a ward with 10 beds and print the count to verify.

## Expected Output
```text
Ward: Intensive Care Unit
Capacity: 10 beds created.
```
