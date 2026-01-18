---
title: "Database Transaction Manager - The Finally Block"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 1
difficulty: easy
use_case: guaranteed_cleanup
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["exceptions", "finally", "cleanup"]
  subtopics:
    - resource-management
    - transactions
---

# Lab 1: Database Transaction Manager - The Finally Block

**Objective**: Implement a transaction manager that ensures a simulated database usage flag is always reset (unlocked) even if the transaction fails.

## Generic Information
**Problem Statement**: You have a database that can only handle one writer at a time. You set `db.is_locked = True` before writing. If writing fails, you MUST set `db.is_locked = False`, otherwise the DB stays locked forever ("deadlock").
**Goals**:
- Implement `execute_transaction(db, transaction_func)`.
- Use `try...finally`.
- Ensure `db.is_locked` is False after execution, regardless of exceptions.

## Use Case: Guaranteed Cleanup
A critical "Patient Vitals" recorder needs to lock the record to prevent race conditions. If the recording crashes, the lock must be released so other nurses can update the record.

## Lab Structure
1.  **Mock DB**: A simple class with a boolean lock.
2.  **Transaction Runner**: The function managing the lock lifecycle.
3.  **Failure Simulation**: Testing with a function that raises an error.

## Getting Started
The `finally` block runs even if the `try` block raises an unhandled exception. This is why it's safer than just putting cleanup code after the `except` block.
