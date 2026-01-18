---
title: "Drug Dosing Calculator - Arithmetic Errors"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 3
difficulty: intermediate
use_case: robust_calculation
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["exceptions", "math", "ZeroDivisionError"]
  subtopics:
    - input-validation
    - error-propagation
---

# Lab 3: Drug Dosing Calculator - Arithmetic Errors

**Objective**: Create a medication dosage calculator that prevents crashes from invalid arithmetic operations, specifically division by zero.

## Generic Information
**Problem Statement**: Dosage calculations often involve formulas like `Total Dose / Frequency`. If a user enters `0` for frequency, the program crashes with `ZeroDivisionError`. Additionally, inputs might be non-numeric strings. We need a robust calculator that handles both.
**Goals**:
- Implement `calculate_dose_per_intake(total_mg, frequency)`.
- Handle `ZeroDivisionError` (frequency is 0).
- Handle `TypeError` or `ValueError` (inputs are strings or None).
- Use the `else` clause to round the result only if the calculation succeeded.

## Use Case: Robust Calculation
The pharmacy system calculates per-intake dosages. A robust system ensures no runtime errors occur during critical dispensing operations.

## Lab Structure
1.  **Calculation Logic**: Performing the division.
2.  **Exception Handling**: Catching math and type errors.
3.  **Success Logic**: Using `else` to format the valid result.

## Getting Started
The `else` block is perfect here. You don't want to try rounding a `None` result or a string, so put the rounding logic in `else` where you know `result` is a valid number.
