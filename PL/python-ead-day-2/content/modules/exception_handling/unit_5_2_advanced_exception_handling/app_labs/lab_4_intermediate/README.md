---
title: "Redundant Data Fetcher - Nested Try-Except"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 4
difficulty: intermediate
use_case: fault_tolerance
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["exceptions", "nested-try", "fallback"]
  subtopics:
    - resilience
    - control-flow
---

# Lab 4: Redundant Data Fetcher - Nested Try-Except

**Objective**: Implement a fault-tolerant logic that attempts to fetch data from a primary source, and falls back to a secondary source if the first fails, using nested exception handlers.

## Generic Information
**Problem Statement**: Distributed systems fail. If `PrimaryServer` is down, we must try `BackupServer`. If `BackupServer` is also down, then we fail completely. This requires a "Try, Catch -> Try, Catch -> Fail" structure.
**Goals**:
- Implement `fetch_data(sources)`.
- Use an outer `try-except` for the primary source.
- Use an inner `try-except` (inside the `except` block) for the backup source.

## Use Case: Fault Tolerance
A "LabResults" viewer tries to pull data from the "LiveDB". If it's undergoing maintenance, it switches to the "ArchiveDB".

## Lab Structure
1.  **Sources**: Mock functions that might fail.
2.  **Logic**: Nested handlers.
3.  **Outcome**: Successful data or a final "All systems down" error.

## Getting Started
While nested try-excepts can be messy, they are a direct way to model "Plan A, then Plan B".
