---
title: "The Hospital Bed Identity"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 2
difficulty: easy
use_case: identity-vs-state
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["identity", "state", "instance"]
---

# Lab 2: The Hospital Bed Identity

**Module**: Thinking in Objects
**Objective**: Understand the difference between an object's **State** (the data it holds) and its **Identity** (its unique existence in memory).
**Difficulty**: Easy
**Context**: Asset Management

## Problem Statement
A hospital has thousands of identical beds. They are the same model, same color, and same price. However, Bed #1 is NOT Bed #2. They are physically distinct.

In this lab, you will create a `Bed` class. You will then create two bed objects with identical attributes and prove that Python treats them as distinct entities.

## Requirements
1.  **Class Definition**: Create a `Bed` class with attributes `model` and `is_occupied`.
2.  **State vs Identity**: 
    - Create `bed1` and `bed2` (both "Standard" model).
    - Print their attributes to show they have the same **State**.
    - Compare them using `is` and print their `id()` values to show they have different **Identities**.

## Expected Output
```text
Bed 1 State: Standard | Bed 2 State: Standard
Identity Check (bed1 is bed2): False
Bed 1 Memory ID: 1407...
Bed 2 Memory ID: 1408...
```
