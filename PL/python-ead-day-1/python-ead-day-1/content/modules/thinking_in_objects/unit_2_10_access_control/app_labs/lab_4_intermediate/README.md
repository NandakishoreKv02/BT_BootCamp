---
title: "The Dynamic Vitals Formatter"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 4
difficulty: intermediate
use_case: complex-property
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["property-logic", "formatting", "encapsulation"]
---

# Lab 4: The Dynamic Vitals Formatter

**Module**: Thinking in Objects
**Objective**: Build a `@property` that does not just return raw data, but processes it on-the-fly.
**Difficulty**: Intermediate
**Context**: Critical Care Monitoring

## Problem Statement
A `VitalsMonitor` stores the `temperature` in Celsius internally. However, for some clinicians, we need to display it as a formatted string with the unit (e.g., "37.0 °C"). 

Additionally, we want to create a property `is_fever` that returns a boolean based on the current internal temperature.

## Requirements
1.  **Modeling**:
    - Class `VitalsMonitor`.
2.  **Implementation**:
    - Manage `_temp` internally.
    - Property `display_temp`: returns "{val} °C".
    - Property `is_fever`: returns `True` if `_temp > 38.0`.
3.  **Encapsulation**:
    - Direct access to `_temp` should be avoided for reporting.

## Expected Output
```text
Reading: 37.5 °C
Fever Detected: False

Reading: 39.0 °C
Fever Detected: True
```
