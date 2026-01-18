---
title: "Secure File Processor - Context Managers"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 5
difficulty: advanced
use_case: automated_cleanup
domain: healthcare
order: 5
duration_hours: 2.0
tags:
  topics: ["exceptions", "with-statement", "context-lib"]
  subtopics:
    - file-io
    - pythonic-patterns
---

# Lab 5: Secure File Processor - Context Managers

**Objective**: Replace verbose `try-finally` file handling code with the clean `with` statement (Context Manager) pattern, ensuring files are always closed even when processing errors occur.

## Generic Information
**Problem Statement**: Manual `file.close()` in `finally` blocks is tedious and error-prone (if you forget it, you leak resources). Python's `with open(...)` automatically handles this.
**Goals**:
- Implement `process_patient_file(filepath)`.
- Use the `with` statement to open the file.
- Read lines and process them.
- Handle `ValueError` (simulating corrupt data lines) without breaking the loop (skipping bad lines) OR letting the whole usage fail—design choice: For this lab, if a line is bad, log it and continue.
- BUT if the file is missing, catch `FileNotFoundError`.

## Use Case: Automated Cleanup
The "ChartImporter" reads daily logs. It must never leave a half-open file handle, as the logs are rotated nightly.

## Lab Structure
1.  **Context Manager**: Using `with open`.
2.  **Line Processing**: Iterating and parsing.
3.  **Exception Handling**: Catching specific parsing errors.

## Getting Started
`with open(f) as file:` is syntactic sugar for `file = open(f); try: ... finally: file.close()`.
