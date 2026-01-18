---
title: "The Flexible Registrar"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 1
difficulty: easy
use_case: default-arguments
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["overloading", "default-arguments", "clean-code"]
---

# Lab 1: The Flexible Registrar

**Module**: Thinking in Objects
**Objective**: Use default arguments to handle cases where some clinical data might be missing during registration.
**Difficulty**: Easy
**Context**: Patient Registration

## Problem Statement
A `PatientRegistrar` class has a `register` method. 
1.  **Requirement**: Always take a `patient_name`.
2.  **Optional**: Take an `insurance_provider`. If not provided, it should default to "Self-Pay".
3.  **Optional**: Take a `ward_number`. If not provided, it should default to 0 (Outpatient).

You must implement this using a single method definition.

## Requirements
1.  **Architecture**:
    - Class `PatientRegistrar`.
2.  **Implementation**:
    - Constructor requires no arguments.
    - `register(self, name, insurance="Self-Pay", ward=0)`: 
      - Return a formatted string: "Registered {name} (Insurance: {insurance}) to Ward {ward}".

## Expected Output
```text
Registered Alice (Insurance: Self-Pay) to Ward 0
Registered Bob (Insurance: Medicare) to Ward 101
```
