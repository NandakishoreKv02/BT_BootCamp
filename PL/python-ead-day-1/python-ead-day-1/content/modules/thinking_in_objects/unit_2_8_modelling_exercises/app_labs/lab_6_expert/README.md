---
title: "The EHR Refactoring Challenge"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 6
difficulty: expert
use_case: god-object-refactoring
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["cohesion", "refactoring", "modelling"]
---

# Lab 6: The EHR Refactoring Challenge

**Module**: Thinking in Objects
**Objective**: identify a "God Object" (too much responsibility) and refactor it into multiple cohesive, associated classes.
**Difficulty**: Expert
**Context**: Legacy EHR Migration

## Problem Statement
You have inherited a legacy Python class called `MedicalSystem`. It is a "God Object"—it handles patient registration, clinical vitals, and billing payments all in one place. This makes it impossible to maintain.

Your task is to **decompose** this class into three smaller, focused classes that work together through **Associations**.

## Requirements
1.  **Decomposition**:
    - `PatientRegistry`: Responsible ONLY for names and MRNs.
    - `ClinicalNotebook`: Responsible ONLY for storing vitals/notes.
    - `BillingModule`: Responsible ONLY for invoices and payments.
2.  **Implementation**:
    - The main `EHRPlatform` should coordinate these three.
    - Each module should have a clear, focused method (e.g., `register()`, `record_vitals()`, `generate_bill()`).

## Expected Output
```text
Refactoring System...
Registry: John registered [MRN: 101]
Clinical: Vitals recorded for MRN: 101
Billing: Invoice issued for MRN: 101 ($50.0)
```
