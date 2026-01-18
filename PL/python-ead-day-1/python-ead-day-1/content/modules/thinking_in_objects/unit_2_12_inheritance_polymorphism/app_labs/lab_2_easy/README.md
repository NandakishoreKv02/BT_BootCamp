---
title: "The Specialized Stethoscope"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 2
difficulty: easy
use_case: method-overriding
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["overriding", "inheritance", "specialization"]
---

# Lab 2: The Specialized Stethoscope

**Module**: Thinking in Objects
**Objective**: Override a base class method to provide specialized behavior for a medical instrument.
**Difficulty**: Easy
**Context**: Clinical Tools

## Problem Statement
All `MedicalTool` objects have a `use()` method that prints a generic message. However, a `Stethoscope` should provide a specific acoustic message when `use()` is called. You must implement overriding to achieve this.

## Requirements
1.  **Modeling**:
    - Parent: `MedicalTool`.
    - Child: `Stethoscope`.
2.  **Implementation**:
    - `MedicalTool.use()`: returns "Using tool."
    - `Stethoscope.use()`: returns "Listening to heart sounds."
3.  **Instantiation**:
    - Create both objects and call their `use()` method.

## Expected Output
```text
Tool: Using tool.
Stethoscope: Listening to heart sounds.
```
