---
title: "Critical Dosage Auditor"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 6
difficulty: expert
use_case: patient_safety
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["error-handling", "control-flow"]
  subtopics: ["else-block", "finally-block", "audit-logging"]
---

# Lab 6: Critical Dosage Auditor

**Module**: Language Fundamentals  
**Objective**: Use the full suite of error handling tools (`try`, `except`, `else`, `finally`) to create a robust dosage calculation engine that guarantees an audit log is created.  
**Difficulty**: Expert  
**Context**: Healthcare - Medication Administration Record (MAR)

## Generic Information
**Problem Statement**: When calculating a dosage, you must ensure that:
1.  Errors like division by zero or invalid numbers are caught.
2.  Successful calculations are explicitly acknowledged.
3.  An audit log entry is **always** created, regardless of success or failure, to ensure traceability in clinical settings.

## Use Case
**Title**: Safe MAR Calculator  
**Description**: Divide `total_mg` by `volume_ml` to get concentration.

### Rules
- `calculate_concentration(total_mg, volume_ml)`
- **`try`**: Perform `total_mg / volume_ml`.
- **`except (ZeroDivisionError, TypeError)`**: 
  - Print "AUDIT: Calculation Failed".
  - Return `0.0`.
- **`else`**: 
  - Print "AUDIT: Calculation Successful".
  - Return the result.
- **`finally`**: 
  - Print "AUDIT: Transaction Completed".
  - (Note: The `else` and `except` returns will execute, but `finally` runs its print statement before the function actually exits).

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
