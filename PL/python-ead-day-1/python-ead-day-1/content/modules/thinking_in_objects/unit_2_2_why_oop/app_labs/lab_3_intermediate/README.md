---
title: "Patient Record Validator"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 3
difficulty: intermediate
use_case: maintainability
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["maintainability", "validation", "data-integrity"]
---

# Lab 3: Patient Record Validator

**Module**: Thinking in Objects
**Objective**: Demonstrate **Maintainability** by building a validation system that allows developers to add new clinical rules without modifying the core engine.
**Difficulty**: Intermediate
**Context**: Electronic Health Records (EHR) Integrity

## Problem Statement
A hospital needs to validate patient records. Currently, the only rule is that an MRN must be 6 digits. However, the regulatory board will soon require rules for Age (must be positive) and Name (cannot be empty).

If we write one massive "if/else" function, it will become unmaintainable as more rules are added. We need a "Validator Object" that allows rules to be plugged in dynamically.

## Requirements
1.  **Validator State**: Create a `Validator` object (dictionary) that stores a list of "pluggable rules".
2.  **Add Rules**: Create an `add_rule(validator, rule_func)` function to extend the system's capabilities.
3.  **Core Engine**: Implement `run_validation(validator, patient_data)` to execute all stored rules and return any errors found.

## Expected Output
```text
Validating John Doe...
- Error: MRN must be 6 digits
- Error: Age cannot be negative
Validation Failed.
```
(Notice how we can add 100 new rules without ever changing the `run_validation` engine.)
