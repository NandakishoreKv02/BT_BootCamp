---
title: "The Pharmacy Stock System"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 2
difficulty: easy
use_case: full-class-design
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["class-design", "methods", "state-management"]
---

# Lab 2: The Pharmacy Stock System

**Module**: Thinking in Objects
**Objective**: design a class from scratch to manage inventory, demonstrating proper state management and method naming.
**Difficulty**: Easy
**Context**: Hospital Pharmacy

## Problem Statement
You need a `PharmacyManager` that tracks medications.
- It must hold a `stock` dictionary `{"DrugName": quantity}`.
- It needs methods to `add_stock`, `dispense_stock`, and `check_availability`.
- It should fail gracefully if you try to dispense more than you have.

## Requirements
1.  **Class**: `PharmacyManager`.
2.  **Logic**:
    - `dispense_stock(name, amount)`: Return `True` if successful, `False` if insufficient funds (or stock).
    - `add_stock(name, amount)`: Increase the quantity.
3.  **Encapsulation**: Treat the dictionary as internal state.

## Expected Output
```text
Added 100 Aspirin.
Dispensing 20 Aspirin... Success.
Dispensing 90 Aspirin... Failed (Insufficient stock).
```
