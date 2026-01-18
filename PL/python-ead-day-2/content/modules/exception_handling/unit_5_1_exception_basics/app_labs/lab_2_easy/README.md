---
title: "Record Finder - Safe Dictionary Access"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 2
difficulty: easy
use_case: safe_lookup
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["exceptions", "KeyError", "lookup"]
  subtopics:
    - dictionary-access
    - error-messaging
---

# Lab 2: Record Finder - Safe Dictionary Access

**Objective**: Implement a safe lookup system for patient records that handles missing keys gracefully.

## Generic Information
**Problem Statement**: When accessing a nested dictionary structure (e.g., `records[patient_id][field]`), a missing ID or field causes a `KeyError` crash. We need a wrapper function that tries to find the data and returns a friendly "Not Found" message instead of crashing.
**Goals**:
- Implement `get_patient_field(records, patient_id, field)`.
- Use `try-except KeyError` to handle lookups.
- Differentiate between "Patient Not Found" and "Field Not Found" if possible (optional challenge).

## Use Case: Safe Lookup
A backend service queries a JSON blob of medical records. It must be resilient to partial or missing data.

## Lab Structure
1.  **Lookup Logic**: The function attempting the dictionary access.
2.  **Error Handling**: Catching `KeyError`.
3.  **User-Friendly Return**: Translating the exception into a string return value.

## Getting Started
Remember that catching `KeyError` will catch *any* key error inside the try block. If you want to know *which* key failed, you can inspect the exception object `e` or structure your try blocks carefully.
