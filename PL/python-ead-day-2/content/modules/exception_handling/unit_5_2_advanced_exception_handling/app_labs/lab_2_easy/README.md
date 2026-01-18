---
title: "Error Logger - Re-raising Exceptions"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 2
difficulty: easy
use_case: observability
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["exceptions", "re-raise", "logging"]
  subtopics:
    - observability
    - error-propagation
---

# Lab 2: Error Logger - Re-raising Exceptions

**Objective**: Implement a logging middleware that intercepts errors to record them, but allows them to propagate so that the main application logic knows a failure occurred.

## Generic Information
**Problem Statement**: You want to log every error that happens in a calculation function. However, if you catch the error to log it, you effectively "swallow" it (the program continues). You need to catch, log, and then *throw it again*.
**Goals**:
- Implement `calculate_with_logging(a, b, logger)`.
- Catch `ZeroDivisionError`.
- Log "Error occurred" using the logger.
- Re-raise the exception using `raise`.

## Use Case: Observability
Your "VitalsMonitor" runs in the background. If it crashes, you need a local log file record, BUT you also need the main system watchdog to see the crash so it can restart the process.

## Lab Structure
1.  **Mock Logger**: A simple list or class to capturing messages.
2.  **Calculation**: A risky operation.
3.  **Reflective Catch**: Catching and re-raising.

## Getting Started
Remember: `raise` (with no arguments) re-raises the active exception. `raise e` re-raises the specific exception object but changes the stack trace slightly (starting from the `except` block). The bare `raise` is preferred for transparency.
