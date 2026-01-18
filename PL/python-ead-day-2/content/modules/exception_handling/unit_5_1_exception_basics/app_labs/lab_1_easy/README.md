---
title: "Patient Intake Form - Input Validation"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 1
difficulty: easy
use_case: input_validation
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["exceptions", "validation", "try-except"]
  subtopics:
    - ValueError
    - input-cleaning
---

# Lab 1: Patient Intake Form - Input Validation

**Objective**: Implement a robust input parser for a patient registration system that handles invalid data gracefully using `try-except` blocks.

## Generic Information
**Problem Statement**: User input is notoriously unreliable. A user might enter "twenty" instead of "20" for age, or "N/A" for weight. Your application crashes if you try to `int()` these strings directly. You need to "sanitize" this input by catching conversion errors.
**Goals**:
- Create a function `process_intake(raw_data)` that accepts a dictionary of raw strings.
- safely convert `age` to `int` and `weight` to `float`.
- Return a "cleaned" dictionary or a list of error messages if validation fails.

## Use Case: Input Validation
The "ClinicConnect" kiosk collects data. You will build the backend logic that processes the form submission without crashing the kiosk.

## Lab Structure
1.  **Validator Functions**: Helpers to parse numbers safely.
2.  **Main Processor**: Orchestrates the validation for a full record.
3.  **Error Collection**: Aggregating all errors (listing both invalid age AND invalid weight if both occur).

## Getting Started
Remember that `int("abc")` raises `ValueError`. This is the primary exception you will be handling.
