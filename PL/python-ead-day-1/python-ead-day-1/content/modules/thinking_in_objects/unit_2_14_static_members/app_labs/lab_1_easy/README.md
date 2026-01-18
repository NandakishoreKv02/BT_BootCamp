---
title: "The Hospital Bed Counter"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 1
difficulty: easy
use_case: class-variable-state
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["static-variables", "shared-state", "counters"]
---

# Lab 1: The Hospital Bed Counter

**Module**: Thinking in Objects
**Objective**: Implement a class-level variable that tracks the total number of occupied beds across all patient instances.
**Difficulty**: Easy
**Context**: Bed Management

## Problem Statement
A `BedAdmission` object represents a single patient taking a bed. Since the hospital has a physical limit, we need a way to track the total `occupied_beds` that is shared by ALL admissions. Every time a new `BedAdmission` is created, the global count should increase.

## Requirements
1.  **Architecture**:
    - Class `BedAdmission`.
2.  **Implementation**:
    - Define a static variable `occupied_beds = 0`.
    - In `__init__`, increment `BedAdmission.occupied_beds`.
3.  **Verification**:
    - Create three admissions and check the final count from the class name.

## Expected Output
```text
Admitting Patient 1...
Admitting Patient 2...
Admitting Patient 3...
Total Occupied Beds (System-Wide): 3
```
