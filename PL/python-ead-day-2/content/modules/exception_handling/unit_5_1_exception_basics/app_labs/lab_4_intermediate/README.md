---
title: "Inventory Batch Processor - Exception Hierarchy"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 4
difficulty: intermediate
use_case: error_hierarchy
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["exceptions", "LookupError", "hierarchy"]
  subtopics:
    - catching-parent-exceptions
    - list-processing
---

# Lab 4: Inventory Batch Processor - Exception Hierarchy

**Objective**: Learn how to use Python's exception hierarchy to catch multiple related error types (like `IndexError` and `KeyError`) with a single handler.

## Generic Information
**Problem Statement**: You are processing a batch of inventory updates. The updates are a list of dictionaries. You might access a list index that doesn't exist (`IndexError`) or a dictionary key that doesn't exist (`KeyError`). Since both are "lookup" failures, you can catch their common parent class `LookupError`.
**Goals**:
- Implement `process_batch(batch_list, target_index, target_key)`.
- Use `except LookupError` to catch both `IndexError` and `KeyError`.
- Log the specific error message.

## Use Case: Exception Hierarchy
A "PharmacyBot" scans shelves. Sometimes it looks for a shelf that doesn't exist (Index) or a drug bin that isn't labeled (Key). Both are lookup failures handling by the same routine.

## Lab Structure
1.  **Batch Access**: Navigating the nested data structure.
2.  **Parent Catch**: Using `LookupError` instead of two separate `except` blocks.
3.  **Error Details**: Using `as e` to see what actually went wrong.

## Getting Started
`LookupError` is the parent of `IndexError` and `KeyError`. Catching it simplifies your code when the handling logic ("Item not found") is the same for both cases.
