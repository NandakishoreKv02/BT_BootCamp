---
title: "Classifying the Pharmacy System"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 2
difficulty: easy
use_case: bce-classification
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["bce", "architecture", "modeling"]
---

# Lab 2: Classifying the Pharmacy System

**Module**: Thinking in Objects
**Objective**: Build a multi-layered application where classes are strictly categorized into Entity (Data), Boundary (Interface), and Control (Logic).
**Difficulty**: Easy
**Context**: Pharmacy Automation

## Problem Statement
A simple script where one function handles everything is hard to maintain. We want to architect a Pharmacy system using the **BCE** model:
1.  **Entity**: `Prescription` (Holds data like drug name).
2.  **Boundary**: `PharmacyUI` (Handles printing to the user).
3.  **Control**: `DispensingLogic` (Decides if a prescription can be filled).

## Requirements
1.  **Architecture**:
    - Implement the three classes. Each should do ONLY its specific BCE job.
2.  **Logic**:
    - `DispensingLogic` should check if the dose is > 0.
3.  **Interaction**:
    - The `PharmacyUI` should take the result from the `DispensingLogic` and display it.

## Expected Output
```text
PHARMACY TERMINAL: Processing Aspirin...
Result: SUCCESS - Dispensing 50mg
```
