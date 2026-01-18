---
title: "Vital Signs - Operator Overloading"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 3
difficulty: intermediate
use_case: medical_device_interface
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["oop", "polymorphism", "operator-overloading"]
  subtopics:
    - dunder-comparison
    - custom-object-math
    - unit-validation
---

# Lab 3: Vital Signs - Operator Overloading

**Objective**: Overload comparison operators to allow direct comparison of vital sign objects.

## Generic Information
**Problem Statement**: We have `VitalSign` objects (e.g., Blood Pressure: 120 mmHg). Currently, to check if a patient is critical, we write `if patient.bp.value > threshold.value`. It would be cleaner to write `if patient.bp > threshold`.
**Goals**:
- Create a `VitalSign` class.
- Overload `__gt__` (greater than) and `__lt__` (less than).
- Implement string representation `__str__`.

## Use Case: Critical Alerts
- **VitalSign**: Has `value` (float) and `unit` (str).
- **Comparison**: `VitalSign(150, "mmHg") > VitalSign(120, "mmHg")` should be `True`.
- **Safety**: Should raise error if units don't match.

## Lab Structure
1.  **VitalSign Class**: Init with value/unit.
2.  **Comparison Logic**: Implement dunder methods with unit validation.
3.  **Alert Check**: Function taking reading and threshold.
