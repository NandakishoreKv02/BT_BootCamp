---
title: "Medical Record System - String Representations"
type: app_lab
module: oop
unit: unit_3_4_special_methods
lab_number: 1
difficulty: easy
use_case: medical_record_system
domain: healthcare
order: 1
duration_hours: 1.5
tags:
  topics: ["oop", "special-methods", "dunder-methods"]
  subtopics:
    - str-method
    - repr-method
    - string-representation
---

# Lab 1: Medical Record System - String Representations

**Module**: Object-Oriented Programming - Part 1
**Objective**: Implement `__str__` and `__repr__` for medical record classes
**Difficulty**: Easy
**Context**: Healthcare - Medical Record System

## Generic Information

**Problem Statement**: A hospital's medical record system needs consistent, readable output for patient records. Staff need user-friendly displays for patient information, while developers need detailed representations for debugging and logging.

**Goals**:
- Implement `__str__` for user-friendly patient display
- Implement `__repr__` for developer debugging
- Understand the difference between the two methods
- Create consistent string output across the system

**Data Elements**:
- Patient ID (string)
- Name (string)
- Date of Birth (string)
- Blood Type (string)
- Admission Date (string)

## Use Case

**Title**: Display Patient Records

**Description**: Medical staff view patient summaries on screens and in reports. The system must provide clean, readable output for daily use, while also supporting detailed debug output for IT staff troubleshooting issues.

### Rules
- `__str__` should return human-readable format
- `__repr__` should return constructor-style format
- Both methods must include key identifying information
- Output must be consistent and predictable

### Test Cases
- Case 1: Print patient shows friendly format
- Case 2: repr(patient) shows debug format
- Case 3: Patient in list shows repr format

### Success Criteria
- `print(patient)` shows user-friendly output
- `repr(patient)` shows reconstructable output
- All patient attributes accessible in output

## Task Summary

- **Task 1**: Create Patient class with attributes
- **Task 2**: Implement `__str__` method
- **Task 3**: Implement `__repr__` method
- **Task 4**: Test both representations

## Getting Started

```python
patient = Patient("P001", "Alice Smith", "1990-05-15", "O+", "2024-01-10")
print(patient)       # Patient: Alice Smith (ID: P001)
print(repr(patient)) # Patient('P001', 'Alice Smith', '1990-05-15', 'O+', '2024-01-10')
```
