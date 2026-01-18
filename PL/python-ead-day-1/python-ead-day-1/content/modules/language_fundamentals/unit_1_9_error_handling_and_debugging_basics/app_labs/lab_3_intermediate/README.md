---
title: "Insurance Coverage Lookup"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 3
difficulty: intermediate
use_case: billing
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["error-handling", "dictionaries"]
  subtopics: ["keyerror", "logging"]
---

# Lab 3: Insurance Coverage Lookup

**Module**: Language Fundamentals  
**Objective**: Handle missing keys in a patient dictionary and log the event for administrative review.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Revenue Cycle Management (RCM)

## Generic Information
**Problem Statement**: When processing a claim, you need to check the "provider_id". Some patient records are incomplete and missing this key. Instead of using `.get()`, you will use `try/except` to demonstrate specific error trapping and secondary actions (like printing a log).

## Use Case
**Title**: Provider ID Finder  
**Description**: Retrieve the provider ID from a record.

### Rules
- `fetch_provider_id(patient_record)`
- Try to return `patient_record["provider_id"]`.
- If `KeyError` occurs:
  1. Print "LOG: Missing provider ID for patient {name}" (where name is from the "name" key).
  2. Return `"PENDING_VERIFICATION"`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
