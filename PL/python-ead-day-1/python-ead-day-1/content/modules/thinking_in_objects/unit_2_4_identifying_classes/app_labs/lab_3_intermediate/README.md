---
title: "Breaking the God Object"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 3
difficulty: intermediate
use_case: refactoring-complexity
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["cohesion", "refactoring", "single-responsibility"]
---

# Lab 3: Breaking the God Object

**Module**: Thinking in Objects
**Objective**: Identify a "God Object" (a class that does too much) and refactor it into multiple, smaller, highly cohesive classes.
**Difficulty**: Intermediate
**Context**: Hospital Administration Refactoring

## Problem Statement
The legacy code has a class called `HospitalApp`. It stores patient info, handles bed assignments, and calculates bills. This violates the **Single Responsibility Principle**. If you change how billing works, you might accidentally break the bed management list.

Your task is to decompose `HospitalApp` into three distinct classes:
1.  `Patient` (Entity)
2.  `Ward` (Entity/Control)
3.  `BillingEngine` (Control)

## Requirements
1.  **Decomposition**: Move the attributes and methods from the messy `HospitalApp` into the appropriate new classes.
2.  **Encapsulation**: Each new class should only have data and methods relevant to its specific domain.
3.  **Collaboration**: The `Ward` should be able to store `Patient` objects.

## Expected Output
```text
Patient: John Doe, Bed: 101, Bill: $500.0
```
(Notice how three independent classes collaborate to produce the result.)
