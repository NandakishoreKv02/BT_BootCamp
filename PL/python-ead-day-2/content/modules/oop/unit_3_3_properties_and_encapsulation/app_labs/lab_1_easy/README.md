---
title: "Patient Vital Signs Monitor - Basic Properties"
type: app_lab
module: oop
unit: unit_3_3_properties_and_encapsulation
lab_number: 1
difficulty: easy
use_case: patient_vital_signs_monitoring
domain: healthcare
order: 1
duration_hours: 1.5
tags:
  topics: ["oop", "properties", "encapsulation"]
  subtopics:
    - property-decorator
    - getters
    - basic-encapsulation
    - private-attributes
---

# Lab 1: Patient Vital Signs Monitor - Basic Properties

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master basic property decorators and getters for controlled attribute access
**Difficulty**: Easy
**Context**: Healthcare - Patient Vital Signs Monitoring

## Generic Information

**Problem Statement**: A hospital needs to track patient vital signs (temperature, heart rate, blood pressure). The system must provide controlled access to these sensitive medical data points to prevent accidental modification and ensure data integrity.

**Goals**:
- Implement basic properties with getters
- Use private attributes to store internal state
- Provide read-only access to vital signs data
- Understand the @property decorator

**Data Elements**:
- Patient ID (string)
- Temperature in Celsius (float)
- Heart Rate in BPM (integer)
- Blood Pressure Systolic/Diastolic (integers)

## Use Case

**Title**: Read Patient Vital Signs

**Description**: Medical staff need to view patient vital signs that have been recorded by monitoring equipment. The data should be accessible through properties but not directly modifiable to prevent accidental changes to medical records.

### Rules
- All vital signs stored in private attributes (prefixed with underscore)
- Provide property getters for read-only access
- Temperature must be stored and retrieved as float
- Heart rate and blood pressure as integers
- Patient ID is immutable once set

### Test Cases
- Case 1: Create patient vitals and read temperature
- Case 2: Access heart rate through property
- Case 3: Read blood pressure values
- Case 4: Verify patient ID is accessible

### Success Criteria
- All vital signs accessible through properties
- Direct attribute access to private variables fails
- Properties return correct data types
- Code is clean and follows encapsulation principles

## Overview

This lab introduces you to Python's `@property` decorator for creating getter methods. You'll build a `VitalSigns` class that stores patient vital signs in private attributes and exposes them through read-only properties.

This is a foundational exercise focused on understanding how properties provide controlled access to object attributes.

## Learning Goals

- Understand the `@property` decorator syntax
- Practice creating private attributes with underscore prefix
- Implement getter methods for read-only access
- Apply encapsulation principles to healthcare data
- Learn when to use properties vs direct attributes

## The Scenario

A hospital's patient monitoring system receives vital signs data from medical equipment. This data needs to be stored securely and accessed in a controlled manner. Medical staff should be able to read vital signs but not accidentally modify historical readings.

You'll create a `VitalSigns` class that:
- Stores vital signs in private attributes
- Provides property getters for read access
- Ensures data integrity through encapsulation

## What You'll Build

A `VitalSigns` class with:
- Private attributes for temperature, heart rate, and blood pressure
- Property getters for each vital sign
- Proper initialization with patient data
- Read-only access to all measurements

## How to Use This Lab

1. **Read** `README.md` (this file) for overview
2. **Review** `tasks.md` for specific requirements
3. **Start** with `starter_code.py`
4. **Implement** each task one by one
5. **Run** `tests.py` to verify each task
6. **Compare** your solution with `solution/solution.py`

## Task Summary

- **Task 1**: Create VitalSigns class with private attributes
- **Task 2**: Implement temperature property getter
- **Task 3**: Implement heart_rate property getter
- **Task 4**: Implement blood_pressure property getter (returns formatted string)
- **Task 5**: Add patient_id as read-only property

## Getting Started

```python
# Example usage of what you'll build
vitals = VitalSigns("P12345", 37.2, 72, 120, 80)
print(vitals.temperature)  # 37.2
print(vitals.heart_rate)   # 72
print(vitals.blood_pressure)  # "120/80"
```

## Learning Resources

- Python @property decorator documentation
- Encapsulation principles in OOP
- Private attributes in Python (underscore convention)

## Next Steps

After completing this lab, you'll move to Lab 2 where you'll add setter methods and validation to make properties writable with constraints.
