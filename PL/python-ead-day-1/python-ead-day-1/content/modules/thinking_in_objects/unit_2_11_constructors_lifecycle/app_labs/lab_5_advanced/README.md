---
title: "The Comprehensive Surgical Profile"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 5
difficulty: advanced
use_case: robust-constructor-design
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["keyword-arguments", "defaults", "validation", "initialization"]
---

# Lab 5: The Comprehensive Surgical Profile

**Module**: Thinking in Objects
**Objective**: Build a robust constructor that handles mandatory data, optional data, and automatic timestamping.
**Difficulty**: Advanced
**Context**: Surgical Case Management

## Problem Statement
A `SurgicalCase` is complex. 
- **Mandatory**: Patient name, Procedure.
- **Optional**: Lead surgeon (default: "TBD"), Room number (default: 0).
- **Automatic**: The object must store the character length of the procedure name as a `complexity_score`.

## Requirements
1.  **Architecture**:
    - Class `SurgicalCase`.
2.  **Implementation**:
    - Constructor with mixed mandatory and optional parameters.
    - Automatic calculation of `complexity_score` inside `__init__`.
3.  **Instantiation**:
    - Create a case for "John Doe" with procedure "Appendectomy" using defaults.
    - Create a case for "Jane Doe" with procedure "Cardiac Bypass" specifying surgeon "Dr. House" and room 101.

## Expected Output
```text
Case 1: John Doe | Proc: Appendectomy | Surgeon: TBD | Complexity: 12
Case 2: Jane Doe | Proc: Cardiac Bypass | Surgeon: Dr. House | Complexity: 14
```
