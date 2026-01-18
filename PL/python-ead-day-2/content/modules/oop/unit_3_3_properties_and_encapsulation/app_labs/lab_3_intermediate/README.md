---
title: "Patient Health Metrics - Computed Properties"
type: app_lab
module: oop
unit: unit_3_3_properties_and_encapsulation
lab_number: 3
difficulty: intermediate
use_case: patient_vital_signs_monitoring
domain: healthcare
order: 3
duration_hours: 2.5
tags:
  topics: ["oop", "properties", "computed-values"]
  subtopics:
    - read-only-properties
    - computed-properties
    - dependent-values
    - health-metrics
---

# Lab 3: Patient Health Metrics - Computed Properties

**Objective**: Master read-only and computed properties for derived health metrics
**Difficulty**: Intermediate

## Generic Information

**Problem Statement**: Beyond raw vital signs, medical staff need computed health metrics like BMI, risk scores, and status indicators that are automatically calculated from base measurements.

**Goals**:
- Create read-only computed properties
- Implement dependent property calculations
- Build health risk assessment logic
- Understand when to compute vs store values

## Use Case

**Title**: Calculate Patient Health Metrics

**Description**: Automatically compute BMI, health risk level, and status indicators from vital signs and patient data without storing redundant information.

### Rules
- BMI computed from weight and height
- Risk level based on vital signs ranges
- Status automatically determined from current vitals
- All computed properties are read-only
- Values update automatically when base data changes

## Task Summary

- **Task 1**: Add height and weight properties
- **Task 2**: Implement BMI computed property
- **Task 3**: Create risk_level computed property
- **Task 4**: Add status indicator property
- **Task 5**: Implement is_critical read-only property
