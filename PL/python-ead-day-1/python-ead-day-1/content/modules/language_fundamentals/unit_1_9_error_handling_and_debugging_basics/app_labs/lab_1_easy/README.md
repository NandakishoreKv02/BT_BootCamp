---
title: "Patient Weight Input Guard"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 1
difficulty: easy
use_case: data_validation
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["error-handling", "type-conversion"]
  subtopics: ["try-except", "valueerror"]
---

# Lab 1: Patient Weight Input Guard

**Module**: Language Fundamentals  
**Objective**: Use a `try/except` block to safely convert raw user input (string) into a numeric weight (float).  
**Difficulty**: Easy  
**Context**: Healthcare - Patient Intake

## Generic Information
**Problem Statement**: When patients or staff enter weights through a terminal or web form, they sometimes enter invalid text (e.g., "75kg" instead of just "75"). Your program must handle this without crashing.

## Use Case
**Title**: Clean Weight Parser  
**Description**: Convert a string to a float. If it fails, return 0.0 and print a warning.

### Rules
- `parse_weight(input_str)`
- If successful: Return the float.
- If `ValueError` occurs: Print "Invalid input: {input_str}" and return `0.0`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
