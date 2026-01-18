---
title: "The Abstract Device Blueprint"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 1
difficulty: easy
use_case: basic-abc
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["abc", "abstraction", "contracts"]
---

# Lab 1: The Abstract Device Blueprint

**Module**: Thinking in Objects
**Objective**: Use the `abc` module to create an Abstract Base Class (ABC) that prevents direct instantiation of a generic medical device.
**Difficulty**: Easy
**Context**: Hardware Inventory

## Problem Statement
A hospital has many types of hardware (Monitors, Pumps, Scanners). We need a base class `MedicalDevice` that defines what every device MUST do. However, a "MedicalDevice" itself doesn't exist in the real world—only specific types do. You must ensure no one can create a `MedicalDevice` object directly.

## Requirements
1.  **Imports**:
    - Import `ABC` and `abstractmethod` from `abc`.
2.  **Architecture**:
    - Class `MedicalDevice(ABC)`.
3.  **Implementation**:
    - `@abstractmethod operate(self)`: Define the method but leave it empty (`pass`).
    - Standard method `get_status(self)`: Return "System Ready".

## Expected Output
```text
Attempting to create generic device...
SUCCESS: TypeError raised as expected.
```
