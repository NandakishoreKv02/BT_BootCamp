---
title: "Patient Data Importer - Custom Attributes"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 5
difficulty: advanced
use_case: complex_error_context
domain: healthcare
order: 5
duration_hours: 2.0
tags:
  topics: ["exceptions", "attributes", "parsing"]
  subtopics:
    - context-preservation
    - data-recovery
---

# Lab 5: Patient Data Importer - Custom Attributes

**Objective**: Build a data importer that tracks exactly which row and field failed in a CSV-like structure by attaching this metadata to a custom `ImportError`.

## Generic Information
**Problem Statement**: If you import 10,000 patient records and get a generic `ValueError`, you don't know which record failed. You need to catch the error, and re-raise a custom exception that says "Error on Row 45: Column 'Age' is negative".
**Goals**:
- Define `RecordImportError` with `row_idx` and `field` attributes.
- Implement `validate_record(row_data, row_idx)`.
- Use the attributes in the final error report.

## Use Case: Complex Error Context
The "EMR-Sync" tool processes bulk record updates. It needs to provide a list of missed records to the user so they can fix them and re-upload.

## Lab Structure
1.  **Rich Exception**: Storing index and field.
2.  **Validator**: Checking constraints (e.g., age > 0).
3.  **Importer**: Iterating over multiple records and reporting failures.

## Getting Started
Remember to use `super().__init__(message)` and also set `self.row_idx = row_idx` in the `__init__`.
