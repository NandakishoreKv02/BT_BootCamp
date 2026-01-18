---
title: "The Patient Monitor State Machine"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 4
difficulty: intermediate
use_case: simulation
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["state-management", "dictionaries", "logic"]
---

# Lab 4: The Patient Monitor State Machine

**Module**: Thinking in Objects
**Objective**: Implement a patient monitor simulation where the "Monitor" is a dictionary holding its state (e.g., status: Normal -> Warning -> Critical).
**Difficulty**: Intermediate
**Context**: ICU Monitoring

## Problem Statement
A monitor tracks vitals and changes state.
We want to simulate this monitor. Instead of a global `current_status`, we want to create a `monitor` dict and pass it to a `update_status(monitor)` function which simulates random vital fluctuations.

## Requirements
1.  **Constructor**: `make_monitor(patient_name)` returning `{'name': ..., 'hr': 70, 'status': 'Normal'}`.
2.  **Logic**: `simulate_heart_rate(monitor)`:
    - Increases HR by 10 (simulation).
    - If HR > 100, set status "Warning".
    - If HR > 120, set status "Critical".
3.  **Simulation**: Run the cycle 5 times and print the state changes.

## Expected Output
```text
[John]: HR 80 (Normal)
[John]: HR 110 (Warning)
[John]: HR 130 (Critical)
```
