---
title: "Multi-Level Data Deep Diver"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 5
difficulty: advanced
use_case: complex_data_parsing
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["error-handling", "nested-data"]
  subtopics: ["keyerror", "typeerror", "valueerror"]
---

# Lab 5: Multi-Level Data Deep Diver

**Module**: Language Fundamentals  
**Objective**: Handle multiple possible points of failure in a deeply nested dictionary structure.  
**Difficulty**: Advanced  
**Context**: Healthcare - Electronic Health Record (EHR) Integration

## Generic Information
**Problem Statement**: When receiving a JSON-like object from a 3rd party API, the structure is often unpredictable. Some levels of the dictionary might be missing (`KeyError`), or a value you expect to be a number might be `None` (`TypeError`).

## Use Case
**Title**: Nested Vital Extractor  
**Description**: Extract the weight value from a complex structure.

### Structure
`{"patient": {"observations": {"weight": "70.5"}}}`

### Rules
- `extract_weight(data)`
- Attempt to navigate to `data["patient"]["observations"]["weight"]`.
- Convert that value to a `float`.
- Possible Exceptions:
  - `KeyError`: One of the three keys is missing. Return `"DATA_MISSING"`.
  - `ValueError`: The weight value exists but is not a number (e.g., "Unknown"). Return `"INVALID_FORMAT"`.
  - `TypeError`: The value is `None` or not a string/number. Return `"TECHNICAL_ERROR"`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
