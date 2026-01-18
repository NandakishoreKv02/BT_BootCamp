---
title: "The Smart Diagnostic Dispatcher"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 5
difficulty: advanced
use_case: type-based-dispatching
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["overloading", "type-checking", "isinstance", "dispatching"]
---

# Lab 5: The Smart Diagnostic Dispatcher

**Module**: Thinking in Objects
**Objective**: Simulate "Type Overloading" by creating a single method that executes different clinical logic based on whether the input is a primitive `int` or a custom `object`.
**Difficulty**: Advanced
**Context**: Result Retrieval

## Problem Statement
A `DiagnosticCenter` has a `fetch_details` method. 
- If passed an **integer**, it should treat it as a `report_id` and return "Reading Report ID: {id}".
- If passed a **dictionary**, it should treat it as a `filter_criteria` and return "Searching metrics for: {criteria_keys}".

You must use `isinstance()` inside the method to achieve this "Overloaded" behavior.

## Requirements
1.  **Modeling**:
    - Class `DiagnosticCenter`.
2.  **Implementation**:
    - `fetch_details(self, query)`:
      - Branch logic based on `isinstance(query, int)` vs `isinstance(query, dict)`.
3.  **Error Handling**:
    - If passed an unsupported type, raise a `TypeError`.

## Expected Output
```text
Center Result: Reading Report ID: 500
Center Result: Searching metrics for: ['date', 'type']
ERROR: Unsupported query type!
```
