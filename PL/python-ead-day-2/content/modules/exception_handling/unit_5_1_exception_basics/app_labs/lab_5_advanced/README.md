---
title: "Medical Record Parser - Advanced Exception Handling"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 5
difficulty: advanced
use_case: complex_parsing
domain: healthcare
order: 5
duration_hours: 2.0
tags:
  topics: ["exceptions", "multiple-except", "else", "clean-architecture"]
  subtopics:
    - strict-validation
    - atomic-operations
---

# Lab 5: Medical Record Parser - Advanced Exception Handling

**Objective**: Build a robust parser for raw medical record text strings that handles malformed data, strict type requirements, and logic errors using comprehensive exception handling patterns.

## Generic Information
**Problem Statement**: You receive a raw string like `"ID:101;AGE:45;BP:120/80"`. You need to parse this into a dictionary object. The format is strict. Many things can go wrong: missing delimiters, invalid numbers, missing fields. A single generic `try-except` is bad practice here. You need specific handlers for specific parsing stages.
**Goals**:
- Implement `parse_record(raw_string)`.
- Use specific exceptions (`ValueError`, `IndexError`) for different parsing failures.
- Use `else` to perform the final object creation only if parsing succeeded.

## Use Case: Complex Parsing
The "LegacySystem" exports data as weird text strings. Your modern app needs to ingest this without crashing on the messy data.

## Lab Structure
1.  **Tokenizer**: Splitting the string (can raise `ValueError` if format is bad).
2.  **Field Extractor**: Getting values (can raise `IndexError` if parts missing).
3.  **Type Converter**: Casting to int/float (can raise `ValueError`).
4.  **Orchestrator**: Bringing it together with structured error handling.

## Getting Started
Don't wrap the whole function in one `try`. Try to isolate the "split" logic from the "int conversion" logic if you want to give specific error messages like "Bad Format" vs "Bad Number".
