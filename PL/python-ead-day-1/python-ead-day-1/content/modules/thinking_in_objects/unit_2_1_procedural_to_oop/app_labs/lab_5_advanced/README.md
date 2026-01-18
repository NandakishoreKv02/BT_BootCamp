---
title: "The Pharmacy Interaction"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 5
difficulty: advanced
use_case: modeling
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["interaction", "data-structures", "encapsulation"]
---

# Lab 5: The Pharmacy Interaction

**Module**: Thinking in Objects
**Objective**: Model a complex interaction (dispensing medication) using strictly structural programming.
**Difficulty**: Advanced
**Context**: Pharmacy Management

## Problem Statement
We need a system where a `Pharmacy` has `Inventory`. A `Patient` has a `PrescriptionList`.
Dispensing an item moves it from Inventory to Patient, but only if they have a valid ID.

## Requirements
1.  **Constructors**: `create_pharmacy()`, `create_patient(name, balance)`.
2.  **Add Stock**: `add_medication(pharmacy, name, price, stock)`.
3.  **Interaction**: `dispense_medication(pharmacy, patient, drug_name)`:
    - Check stock.
    - Check patient funds.
    - Deduct funds, decrease stock, add to patient's `medications` list.

## Expected Output
```text
Alice received 'Amoxicillin'.
Pharmacy Stock 'Amoxicillin': 49
```
