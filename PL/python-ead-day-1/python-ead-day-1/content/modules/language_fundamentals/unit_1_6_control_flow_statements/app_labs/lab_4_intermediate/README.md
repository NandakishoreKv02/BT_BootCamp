---
title: "Lab Result Filter"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 4
difficulty: intermediate
use_case: data_cleansing
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["loops", "control-statements"]
  subtopics: ["continue", "break"]
---

# Lab 4: Lab Result Filter

**Module**: Language Fundamentals  
**Objective**: Process a list of mixed lab values, skipping missing data and stopping at the first critical error.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Laboratory Information System (LIS)

## Generic Information
**Problem Statement**: Lab data often comes in batches. Sometimes values are missing (`None`) or marked as `"N/A"`. You need to process a list of numerical results.

## Use Case
**Title**: Batch Sanitizer  
**Description**: Iterate results. Skip `None`. If a record is `"CRITICAL_ERROR"`, stop all processing. Add valid numbers to a new list.

### Rules
- `sanitize_lab_results(raw_results)`
- Input: `[10, None, 20, "CRITICAL_ERROR", 30]`
- Logic:
  - Loop through results.
  - If item is `None`, use `continue`.
  - If item is `"CRITICAL_ERROR"`, use `break`.
  - Otherwise, add the numeric value to a returned list.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
