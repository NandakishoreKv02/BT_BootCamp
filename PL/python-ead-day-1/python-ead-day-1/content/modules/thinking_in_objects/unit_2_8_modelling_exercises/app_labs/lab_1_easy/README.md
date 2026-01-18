---
title: "The Clinic Inventory"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 1
difficulty: easy
use_case: simple-modelling
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["identification", "modelling", "composition"]
---

# Lab 1: The Clinic Inventory

**Module**: Thinking in Objects
**Objective**: identify nouns and verbs in a scenario to create a simple object model.
**Difficulty**: Easy
**Context**: Primary Care Logistics

## Problem Statement
"A clinic must keep track of its supplies. Every clinic has an inventory. The inventory contains multiple supply items. Each item has a name and a quantity."

Your task is to model this relationship using **Composition**.

## Requirements
1.  **Classes**:
    - `SupplyItem` (name, quantity).
    - `Inventory` (list of SupplyItems).
2.  **Implementation**:
    - The `Inventory` should have a method `add_item(self, name, qty)` which creates a `SupplyItem` internally.
3.  **Validation**:
    - Create an inventory and add "Bandages" and "Syringes".

## Expected Output
```text
Inventory status:
- Bandages: 100
- Syringes: 50
```
