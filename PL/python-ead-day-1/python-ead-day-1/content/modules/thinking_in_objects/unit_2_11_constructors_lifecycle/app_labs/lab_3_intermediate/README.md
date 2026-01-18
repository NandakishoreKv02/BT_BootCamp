---
title: "The Safe Pharmacy Order"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 3
difficulty: intermediate
use_case: sentinel-pattern-collections
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["mutable-defaults", "sentinel-pattern", "initialization"]
---

# Lab 3: The Safe Pharmacy Order

**Module**: Thinking in Objects
**Objective**: Avoid the "Mutable Default Argument" trap when initializing object collections.
**Difficulty**: Intermediate
**Context**: Inpatient Medication Orders

## Problem Statement
A `PharmacyOrder` contains a list of `medications`. If you use `medications=[]` in the constructor, different orders will "Leak" drugs into each other because they share the same list in memory. You must implement the **Sentinel Pattern** to ensure every order has its own independent list.

## Requirements
1.  **Architecture**:
    - Class `PharmacyOrder`.
2.  **Encapsulation**:
    - Use `medications=None` as the default parameter.
    - Inside `__init__`, if it is `None`, assign a new list `[]`.
3.  **Validation**:
    - Create two orders. Add a drug to the first. Verify the second remains empty.

## Expected Output
```text
Order 1 Drugs: ['Aspirin']
Order 2 Drugs: []
(Independence Verified)
```
