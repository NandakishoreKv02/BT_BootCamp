---
title: "The Clinical Converter"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 2
difficulty: easy
use_case: static-method-utilities
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["staticmethod", "utility-functions", "namespace-grouping"]
---

# Lab 2: The Clinical Converter

**Module**: Thinking in Objects
**Objective**: Use `@staticmethod` to create a utility class that groups medical conversion formulas.
**Difficulty**: Easy
**Context**: Lab Standardization

## Problem Statement
A hospital needs a set of standard tools for converting results. Since these tools doesn't belong to any specific patient or machine, they should be "Static." You must implement a `HealthConverter` class with methods for temperature conversion.

## Requirements
1.  **Architecture**:
    - Class `HealthConverter`.
2.  **Implementation**:
    - `@staticmethod c_to_f(celsius)`: Returns `(celsius * 9/5) + 32`.
    - `@staticmethod f_to_c(fahrenheit)`: Returns `(fahrenheit - 32) * 5/9`.
3.  **Namespace Usage**:
    - Call these methods directly from the class name (e.g., `HealthConverter.c_to_f(37)`).

## Expected Output
```text
37C in Fahrenheit: 98.6
101F in Celsius: 38.3
```
