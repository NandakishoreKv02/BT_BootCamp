---
title: "The Parallel Lab Results"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 2
difficulty: easy
use_case: refactoring
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["dictionaries", "lists", "refactoring"]
---

# Lab 2: The Parallel Lab Results

**Module**: Thinking in Objects
**Objective**: Refactor code that uses parallel lists for lab results into a single list of dictionaries (proto-objects).
**Difficulty**: Easy
**Context**: Clinical Laboratory

## Problem Statement
We have separate lists for patient IDs, test names, and test values.
`ids = [...]`, `tests = [...]`, `values = [...]`.
This is error-prone. If we sort by value, the IDs won't match anymore!
We need to create a "Result Object".

## Requirements
1.  **Refactor**: Create `create_lab_result(pid, test_name, value)` that returns a dictionary.
2.  **Replace**: Use a single list `results = []` containing these dicts.
3.  **Process**: Write `print_lab_report(results)` that loops through the list.

## Expected Output
```text
Patient: P001 | Test: Glucose | Value: 95
Patient: P002 | Test: Cholesterol | Value: 190
```
