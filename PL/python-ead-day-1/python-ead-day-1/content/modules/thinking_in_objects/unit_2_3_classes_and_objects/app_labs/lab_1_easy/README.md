---
title: "The Patient Entity"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 1
difficulty: easy
use_case: class-basics
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["class", "object", "attributes"]
---

# Lab 1: The Patient Entity

**Module**: Thinking in Objects
**Objective**: Create your first formal Python class to represent a patient, moving away from unstructured dictionaries.
**Difficulty**: Easy
**Context**: Electronic Health Records (Registration)

## Problem Statement
A hospital is tired of using dictionaries to track patients because keys like `"name"` are sometimes mistyped as `"fullname"`. We need a formal **Class** blueprint to ensure every patient record follows the exact same structure.

## Requirements
1.  **Define Class**: Create a class named `Patient`.
2.  **Constructor**: Implement `__init__(self, name, age, mrn)`.
3.  **Instantiation**: Create two different patient objects from this class.
4.  **Attribute Access**: Print the patient MRNs to the console.

## Expected Output
```text
Registered: John (MRN123)
Registered: Jane (MRN456)
```
