---
title: "The Universal Diagnosis Engine"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 4
difficulty: intermediate
use_case: polymorphism-list-processing
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["polymorphism", "interfaces", "list-iteration"]
---

# Lab 4: The Universal Diagnosis Engine

**Module**: Thinking in Objects
**Objective**: Build a polymorphic process that treats different diagnosis types through a common interface.
**Difficulty**: Intermediate
**Context**: Clinical Decision Support

## Problem Statement
A `DiagnosticOutput` base class has a method `generate_summary()`. You must create two specific subclasses: `PhysicalExam` and `LabExam`. Each should override the summary method. Then, create a "Case File" (a list) containing both types and iterate through them, calling the summary method to demonstrate polymorphism.

## Requirements
1.  **Architecture**:
    - Base: `DiagnosticOutput`.
    - Children: `PhysicalExam`, `LabExam`.
2.  **Specialization**:
    - `PhysicalExam` summary should focus on vital signs.
    - `LabExam` summary should focus on chemical markers.
3.  **Polymorphic Loop**:
    - Use a single `for` loop to process all items in a list.

## Expected Output
```text
Processing case file...
- Summary: Pulse and Reflexes stable.
- Summary: Glucose and Cholesterol within range.
```
