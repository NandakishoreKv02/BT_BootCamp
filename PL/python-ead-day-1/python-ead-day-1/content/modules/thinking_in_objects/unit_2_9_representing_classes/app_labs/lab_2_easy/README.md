---
title: "The Medical Device Registry"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 2
difficulty: easy
use_case: complex-initialization
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["constructor", "attributes", "pep-8"]
---

# Lab 2: The Medical Device Registry

**Module**: Thinking in Objects
**Objective**: Build a class with multiple instance attributes and verify that each instance maintains its own state.
**Difficulty**: Easy
**Context**: Asset Management

## Problem Statement
A hospital needs to track various medical devices (ventilators, monitors, pumps). Each device has a model name, a serial number, a department, and a "status" (e.g., "Active").

## Requirements
1.  **Modeling**:
    - Class `MedicalDevice`.
2.  **Implementation**:
    - The constructor should accept `model`, `serial`, and `dept`.
    - The `status` should always be initialized to "Active" by default (without needing a constructor argument).
3.  **Validation**:
    - Create two devices and print their details.

## Expected Output
```text
Device 1: Ventilator (S/N: V-77) - Dept: ICU [Status: Active]
Device 2: Infusion Pump (S/N: P-20) - Dept: ER [Status: Active]
```
