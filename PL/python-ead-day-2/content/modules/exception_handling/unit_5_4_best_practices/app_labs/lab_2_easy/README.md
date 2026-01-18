---
title: "The Specific Handler - Clean Scoping"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 2
difficulty: easy
use_case: narrow_scoping
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["exceptions", "specific-handling", "scoping"]
  subtopics:
    - bug-prevention
    - clean-code
---

# Lab 2: The Specific Handler - Clean Scoping

**Objective**: Refactor generic handlers into specific ones and minimize the code inside the `try` block to avoid hiding bugs.

## Generic Information
**Problem Statement**: Catching `Exception` is dangerous because it can hide programming bugs (like `NameError` or `AttributeError`). Also, wrapping a huge block of code in a `try` makes it unclear which line is expected to fail.
**Goals**:
- Narrow the `try` block to only the failing operation.
- Catch the specific exception instead of a generic one.

## Use Case: Narrow Scoping
A "dosage_calculator" reads a record, calculates a dose, and saves it. Only the "calculation" (division) should be in the `try` block for `ZeroDivisionError`. If reading the record fails due to a bug, we *want* the system to crash so we can fix the bug.

## Lab Structure
1.  **Bloated Function**: A function with too much code in a generic `try`.
2.  **Refactor**: Applying narrow scoping.
3.  **Verification**: Ensuring bugs are NOT caught by the handler.

## Getting Started
"Only catch what you know how to handle."
"Keep your try blocks as small as possible."
