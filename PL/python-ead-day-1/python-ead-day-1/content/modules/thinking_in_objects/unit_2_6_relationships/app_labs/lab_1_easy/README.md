---
title: "The Departmental Hierarchy"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 1
difficulty: easy
use_case: inheritance-is-a
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["inheritance", "is-a", "modeling"]
---

# Lab 1: The Departmental Hierarchy

**Module**: Thinking in Objects
**Objective**: Implement an **Is-a** (Inheritance) relationship to model sub-types of hospital departments.
**Difficulty**: Easy
**Context**: Hospital Administration

## Problem Statement
A hospital has many departments. Every department has a `name` and a `location`. However, an `EmergencyDepartment` (ER) specifically needs to track if it is currently "At Capacity" (diverting ambulances).

Your task is to create a base `Department` class and an `EmergencyDepartment` child class that inherits its properties.

## Requirements
1.  **Modeling (Is-a)**:
    - Base Class: `Department` (`name`, `location`).
    - Child Class: `EmergencyDepartment` (Inherits from `Department`).
2.  **Specialization**:
    - The `EmergencyDepartment` should have an extra attribute `is_diverting` (False).
3.  **Inheritance Check**: 
    - Create an ER object and verify it has a name, location, and the diversion flag.

## Expected Output
```text
Department: ER
Location: Wing A
Status: Active (Diverting: False)
```
