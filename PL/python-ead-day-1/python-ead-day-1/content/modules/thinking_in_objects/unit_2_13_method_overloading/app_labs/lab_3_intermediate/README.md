---
title: "The Batch Result Processor"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 3
difficulty: intermediate
use_case: args-variable-arguments
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["args", "variable-arguments", "data-processing"]
---

# Lab 3: The Batch Result Processor

**Module**: Thinking in Objects
**Objective**: Use the `*args` syntax to create a method that can process a variable number of clinical readings.
**Difficulty**: Intermediate
**Context**: Lab Analytics

## Problem Statement
A `LabAnalyzer` needs to calculate the average glucose level from a patient's daily tests. Some days they have 3 tests, other days 10. You must implement a single method `average_glucose` that accepts any number of positional arguments.

## Requirements
1.  **Architecture**:
    - Class `LabAnalyzer`.
2.  **Implementation**:
    - `average_glucose(self, *readings)`:
      - Calculate the sum of all readings.
      - Divide by the number of readings.
      - Return the average.
3.  **Edge Case**:
    - If no readings are provided, return 0.

## Expected Output
```text
Day 1 Average: 110.0
Day 2 Average: 125.5
(Processed 5 total readings)
```
