---
title: "Patient Vital Signs Monitor - Setters & Validation"
type: app_lab
module: oop
unit: unit_3_3_properties_and_encapsulation
lab_number: 2
difficulty: easy
use_case: patient_vital_signs_monitoring
domain: healthcare
order: 2
duration_hours: 2
tags:
  topics: ["oop", "properties", "encapsulation", "validation"]
  subtopics:
    - property-setters
    - data-validation
    - range-checking
    - error-handling
---

# Lab 2: Patient Vital Signs Monitor - Setters & Validation

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master property setters with data validation
**Difficulty**: Easy
**Context**: Healthcare - Patient Vital Signs Monitoring

## Generic Information

**Problem Statement**: Medical equipment updates patient vital signs in real-time. The system must validate all incoming data to ensure measurements are within safe, medically acceptable ranges before storing them.

**Goals**:
- Implement property setters with @property.setter
- Validate vital signs data against medical ranges
- Raise appropriate exceptions for invalid data
- Provide clear error messages for medical staff

**Data Elements**:
- Temperature: 35.0-42.0°C (hypothermia to hyperthermia range)
- Heart Rate: 40-200 BPM (bradycardia to tachycardia range)
- Blood Pressure Systolic: 70-200 mmHg
- Blood Pressure Diastolic: 40-130 mmHg

## Use Case

**Title**: Update Patient Vital Signs with Validation

**Description**: Medical monitoring equipment sends vital signs updates every few minutes. Each measurement must be validated against medically safe ranges before being recorded in the patient's record.

### Rules
- Temperature must be between 35.0°C and 42.0°C
- Heart rate must be between 40 and 200 BPM
- Systolic BP must be between 70 and 200 mmHg
- Diastolic BP must be between 40 and 130 mmHg
- Systolic must be greater than diastolic
- Invalid values raise ValueError with descriptive message

### Test Cases
- Case 1: Valid vital signs update succeeds
- Case 2: Temperature out of range raises ValueError
- Case 3: Heart rate out of range raises ValueError
- Case 4: Invalid blood pressure raises ValueError

### Success Criteria
- All setters validate input before storing
- Invalid data raises ValueError with clear message
- Valid data updates successfully
- Properties remain readable

## Overview

Building on Lab 1, you'll add property setters that validate vital signs data. This ensures only medically valid measurements are stored in patient records.

## Learning Goals

- Implement @property.setter decorators
- Validate numeric ranges
- Raise ValueError with descriptive messages
- Understand validation in healthcare context
- Practice defensive programming

## What You'll Build

An enhanced `VitalSigns` class with:
- Writable properties with validation
- Range checking for all vital signs
- Clear error messages for invalid data
- Safe updates to patient records

## Task Summary

- **Task 1**: Add temperature setter with range validation
- **Task 2**: Add heart_rate setter with range validation
- **Task 3**: Add blood pressure setters with validation
- **Task 4**: Implement set_blood_pressure method with cross-validation
- **Task 5**: Add update_all method for batch updates

## Getting Started

```python
vitals = VitalSigns("P001", 37.0, 70, 120, 80)
vitals.temperature = 38.5  # Valid - updates successfully
vitals.temperature = 45.0  # Invalid - raises ValueError
```
