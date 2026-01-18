---
title: "Enforcing the Scanning Protocol"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 2
difficulty: easy
use_case: concrete-implementation
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["abc", "inheritance", "contracts", "polymorphism"]
---

# Lab 2: Enforcing the Scanning Protocol

**Module**: Thinking in Objects
**Objective**: Implement concrete subclasses of an ABC to fulfill a clinical contract.
**Difficulty**: Easy
**Context**: Radiology Department

## Problem Statement
In the previous lab, we created an abstract `MedicalDevice`. Now, we need to create real devices: an `InfusionPump` and a `HeartMonitor`. Both must implement the `operate()` method to be valid medical tools.

## Requirements
1.  **Inheritance**:
    - Both classes must inherit from `MedicalDevice` (provided in starter).
2.  **Implementation**:
    - `InfusionPump.operate()`: Return "Pumping medication at 5ml/hr".
    - `HeartMonitor.operate()`: Return "Monitoring ECG rhythm...".
3.  **Validation**:
    - Instantiate both and call their `operate()` and `get_status()` methods.

## Expected Output
```text
Pump: Pumping medication at 5ml/hr (Status: System Ready)
Monitor: Monitoring ECG rhythm... (Status: System Ready)
```
