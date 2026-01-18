---
title: "The Configurable Medical Device"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 5
difficulty: advanced
use_case: class-constants-validation
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["static-methods", "class-constants", "validation"]
---

# Lab 5: The Configurable Medical Device

**Module**: Thinking in Objects
**Objective**: Combine static class constants with a static validation method to ensure device safety.
**Difficulty**: Advanced
**Context**: Surgical Robotics

## Problem Statement
A `SurgicalRobot` operates within specific voltage limits. These limits are universal for all robots of this model. You must store these as class constants. You must also implement a `is_safe` static method that verifies if a provided voltage is within the class-defined range.

## Requirements
1.  **Architecture**:
    - Class `SurgicalRobot`.
2.  **Implementation**:
    - Static constants: `MIN_VOLTAGE = 110`, `MAX_VOLTAGE = 240`.
    - `@staticmethod is_safe(voltage)`:
      - Returns `True` if `MIN_VOLTAGE <= voltage <= MAX_VOLTAGE`.
      - Otherwise returns `False`.
3.  **Safety Check**:
    - The constructor should use `is_safe` before setting the instance voltage. If unsafe, it should set voltage to 0 and print a warning.

## Expected Output
```text
Robot 1 initialized at 220V. (Safe: True)
WARNING: Unsafe voltage 300V! Setting to 0.
Robot 2 initialized at 0V. (Safe: False)
```
