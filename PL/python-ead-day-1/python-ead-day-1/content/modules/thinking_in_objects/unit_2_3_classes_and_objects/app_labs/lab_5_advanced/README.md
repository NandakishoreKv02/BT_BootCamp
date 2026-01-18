---
title: "The Prescription Lifecycle"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 5
difficulty: advanced
use_case: state-transitions
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["state-management", "validation", "logic"]
---

# Lab 5: The Prescription Lifecycle

**Module**: Thinking in Objects
**Objective**: manage complex **State Transitions** within an object, ensuring that data can only move between states (e.g., Active to Dispensed) based on valid logical conditions.
**Difficulty**: Advanced
**Context**: Pharmacy Operations

## Problem Statement
A prescription has a lifecycle: It starts as `PENDING`, moves to `FILLED`, and finally to `DISPENSED`. A prescription cannot be dispensed if it is still `PENDING`. It also cannot be filled if it has been marked as `CANCELLED`.

Treating these states as simple strings in a dictionary is risky. We need a `Prescription` class that controls its own lifecycle through methods.

## Requirements
1.  **Class Attributes**: `drug_name`, `dosage`, `status` (initially "PENDING").
2.  **State Control**:
    - `fill()`: Changes status to "FILLED" ONLY if currently "PENDING".
    - `dispense()`: Changes status to "DISPENSED" ONLY if currently "FILLED".
    - `cancel()`: Can change status to "CANCELLED" from any state EXCEPT "DISPENSED".
3.  **Audit Logs**: Each state change should print a confirmation message.

## Expected Output
```text
Filling Amoxicillin... Done (Status: FILLED)
Error: Cannot dispense a PENDING prescription.
```
