---
title: "The Clinical Data Aggregator"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 6
difficulty: expert
use_case: complex-state-aggregation
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["aggregation", "shared-state", "advanced-methods"]
---

# Lab 6: The Clinical Data Aggregator

**Module**: Thinking in Objects
**Objective**: Build a system that manages both individual patient data AND performs real-time aggregation (tracking clinic-wide totals/averages) using class-level state.
**Difficulty**: Expert
**Context**: Population Health Management

## Problem Statement
A clinic needs to track individual patient heart rates, but it also needs to know the **average** heart rate of all patients currently in the building. This requires objects to "talk" to a shared class-level tally.

You will build a `PatientMetric` class that automatically updates a clinic-wide total every time a heart rate is added.

## Requirements
1.  **State Management**:
    - Instance Attributes: `patient_name`, `last_hr`.
    - Class Attributes: `total_hr_sum`, `patient_count`.
2.  **Implementation**:
    - Method `add_reading(self, bpm)`: Updates the instance's `last_hr` BUT also adds to the class's `total_hr_sum`.
3.  **Aggregation**:
    - Method `get_clinic_average()`: A class-level perspective that returns the average across all instances.
4.  **Edge Case**:
    - Ensure your average calculation doesn't crash if no patients are registered (ZeroDivisionError).

## Expected Output
```text
Registered Alice: 70 bpm
Registered Bob: 90 bpm
CLINIC-WIDE AVERAGE: 80.0
```
