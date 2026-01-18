---
title: "The Automatic Vitals Stamper"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 4
difficulty: intermediate
use_case: complex-initialization-logic
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["initialization", "logic-in-init", "constructor"]
---

# Lab 4: The Automatic Vitals Stamper

**Module**: Thinking in Objects
**Objective**: Implement initialization logic that goes beyond simple attribute assignment.
**Difficulty**: Intermediate
**Context**: ER Monitoring

## Problem Statement
A `VitalsReading` object needs to be "Safety Checked" as soon as it is born. If the heart rate is above 100, the constructor should automatically set a `critical_alert` flag to `True`.

## Requirements
1.  **Modeling**:
    - Class `VitalsReading`.
2.  **Implementation**:
    - Constructor accepts `patient_name` and `heart_rate`.
    - **Logic**: If `heart_rate > 100`, initialize `self.critical_alert = True`. Otherwise, set it to `False`.
3.  **Instantiation**:
    - Create a normal reading (75 bpm).
    - Create a critical reading (120 bpm).

## Expected Output
```text
Reading 1: Normal [Alert: False]
Reading 2: Urgent [Alert: True]
```
