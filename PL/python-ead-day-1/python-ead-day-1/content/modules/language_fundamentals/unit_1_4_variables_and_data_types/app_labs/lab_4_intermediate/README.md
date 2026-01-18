---
title: "Data Cleaner"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 4
difficulty: intermediate
use_case: robust_processing
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["type-checking", "exceptions"]
  subtopics: ["isinstance", "try-except"]
---

# Lab 4: Data Cleaner

**Module**: Language Fundamentals  
**Objective**: Build a robust function that safely processes a list of mixed types (dirty data) using `isinstance` and exception handling.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Robust Data Processing

## Generic Information
**Problem Statement**: You receive a list of "Heart Rates" from a device, but due to bugs, the list contains integers, valid strings ("80"), invalid strings ("Error"), and None. You need to sum the valid numbers to calculate an average, ignoring the garbage.

**Goals**:
- Use `isinstance(val, int)` to checks.
- Handle type conversion errors with `try/except`.
- Calculate average safely (avoid divide by zero).

## Use Case
**Title**: Heart Rate Averager
**Description**: Process `[80, "90", "ERR", None, 70]`.

### Rules
- `calculate_average_hr(data_list)`
- Valid items: `int`, or strings that can be converted to `int`.
- Invalid items: `None`, non-numeric strings to be ignored.
- Return: Float (Average of valid items). Return 0.0 if no valid items.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
