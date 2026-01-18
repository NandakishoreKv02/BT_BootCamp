---
title: "The Silent Watcher - Exception Logging"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 3
difficulty: intermediate
use_case: observability
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["exceptions", "logging", "observability"]
  subtopics:
    - traceback-capture
    - logging-config
---

# Lab 3: The Silent Watcher - Exception Logging

**Objective**: Implement production-grade exception logging that captures full tracebacks and context, making production debugging possible.

## Generic Information
**Problem Statement**: In production, `print(e)` is useless. It doesn't tell you the line number, the call stack, or when it happened. Python's `logging` module can capture all of this automatically if used correctly.
**Goals**:
- Use `logging.exception()` to capture full stack traces.
- Differentiate between a simple "Info" log and an "Error" log.

## Use Case: Observability
A "LabResultUploader" connects to a hospital API. If the connection fails, the app shouldn't crash. It should log the *exact reason* (Timeout? DNS? Auth?) so a developer can look at the logs and fix it.

## Lab Structure
1.  **Logger Config**: Setting up basic logging.
2.  **Failure Logic**: A function that fails.
3.  **The Exception Call**: Using `logging.exception()` vs `logging.error()`.

## Getting Started
`logging.exception("msg")` is the same as `logging.error("msg", exc_info=True)`. It captures the current exception traceback automatically.
