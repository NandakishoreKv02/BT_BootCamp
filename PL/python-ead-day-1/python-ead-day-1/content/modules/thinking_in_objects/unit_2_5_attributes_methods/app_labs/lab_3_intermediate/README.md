---
title: "The Prescription Signature"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 3
difficulty: intermediate
use_case: method-signatures
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["methods", "signatures", "validation"]
---

# Lab 3: The Prescription Signature

**Module**: Thinking in Objects
**Objective**: design and implement **Method Signatures** that accept multiple parameters and enforce specific data types.
**Difficulty**: Intermediate
**Context**: Pharmacy Operations

## Problem Statement
A `Prescription` object needs to be updated with clinical precision. A simple `change_dose(10)` isn't enough; we need to know the units (mg, units, ml) and the frequency (once daily, twice daily).

Your task is to design a method with a robust signature that captures all this information and updates the object's state.

## Requirements
1.  **Method Design**:
    - Method `update_instructions(self, dose, unit, frequency)`.
2.  **Logic**:
    - The method should update the attributes and return a formatted string for the pharmacy label.
3.  **Encapsulation**:
    - The attributes should initially be `None` or `0`.

## Expected Output
```text
Updating Prescription for Amoxicillin...
Label: Take 500mg, Twice Daily.
```
