---
title: "Resilient Vital Sign Batch Processor"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 4
difficulty: intermediate
use_case: clinical_analytics
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["error-handling", "loops"]
  subtopics: ["try-except-in-loop", "resilience"]
---

# Lab 4: Resilient Vital Sign Batch Processor

**Module**: Language Fundamentals  
**Objective**: Build a loop that processes a list of raw strings into numbers, skipping and logging any individual failures without stopping the entire task.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Medical Device Interface

## Generic Information
**Problem Statement**: You are importing data from an older blood pressure monitor. Sometimes the data stream contains noise (e.g., `"120"`, `"118"`, `"ERROR_SIGNAL"`, `"122"`). If you try to convert all of them directly, the `ERROR_SIGNAL` will crash your whole loop. You must catch the error inside the loop.

## Use Case
**Title**: Stream Cleaner  
**Description**: Batch convert strings to integers.

### Rules
- `clean_signals(signal_list)`
- Iterate through `signal_list`.
- Try to convert each item to an `int`.
- If successful: Add it to a `cleaned` list.
- If `ValueError` occurs: Print "Skipping corrupt signal: [value]" and `continue`.
- Return the `cleaned` list.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
