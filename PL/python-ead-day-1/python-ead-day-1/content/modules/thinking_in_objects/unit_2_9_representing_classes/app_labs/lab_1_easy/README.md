---
title: "The Patient Blueprint"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 1
difficulty: easy
use_case: class-definition
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["class-definition", "pep-8", "itit"]
---

# Lab 1: The Patient Blueprint

**Module**: Thinking in Objects
**Objective**: Represent a basic class in Python following PEP 8 standards and implementing a constructor.
**Difficulty**: Easy
**Context**: Patient Registration

## Problem Statement
Every hospital information system starts with a simple representation of a patient. Your task is to define a `Patient` class that stores basic information and follows professional Python naming conventions.

## Requirements
1.  **Standardization**:
    - Use PascalCase for the class name.
    - Use snake_case for attributes.
2.  **Implementation**:
    - Define a constructor `__init__` that accepts `patient_id` and `full_name`.
    - Store these values as instance attributes.
3.  **Instantiation**:
    - Create an object for "John Doe" with ID "P-100".

## Expected Output
```text
Patient Registered: John Doe (ID: P-100)
```
