---
title: "Staffing Hierarchy"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 2
difficulty: easy
use_case: is-a-vs-has-a-decision
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["inheritance", "composition", "modelling-decisions"]
---

# Lab 2: Staffing Hierarchy

**Module**: Thinking in Objects
**Objective**: Build a multi-class model and justify the choice between Inheritance (Is-a) and Composition (Has-a).
**Difficulty**: Easy
**Context**: Human Resources

## Problem Statement
A hospital needs to track its staff.
1.  **Inheritance**: A `Physician` is a type of `HospitalStaff`. 
2.  **Composition**: Every `HospitalStaff` has an `IDCard` which is unique to them and managed by the staff object.

## Requirements
1.  **Classes**:
    - `IDCard` (card_number).
    - `HospitalStaff` (name, role).
    - `Physician` (specialty).
2.  **Design**:
    - `Physician` must inherit from `HospitalStaff`.
    - `HospitalStaff` must create its own `IDCard` in `__init__`.

## Expected Output
```text
Staff Name: Dr. Strange
Role: Physician
Specialty: Surgery
ID Card: STAFF-101
```
