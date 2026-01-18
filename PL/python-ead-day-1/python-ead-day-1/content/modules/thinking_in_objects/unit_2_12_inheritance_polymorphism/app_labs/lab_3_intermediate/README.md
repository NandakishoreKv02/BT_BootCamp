---
title: "The Advanced MRI Suite"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 3
difficulty: intermediate
use_case: constructor-super
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["super", "constructor-inheritance", "initialization"]
---

# Lab 3: The Advanced MRI Suite

**Module**: Thinking in Objects
**Objective**: Master the use of `super().__init__()` to properly initialize specialized medical devices.
**Difficulty**: Intermediate
**Context**: Radiology Department

## Problem Statement
A `BasicScanner` requires a `model_name`. An `MRIScanner` is a type of `BasicScanner` that also requires a `tesla_rating` (magnetic field strength). You must use `super()` to ensure the `model_name` is set by the parent while the `tesla_rating` is handled by the child.

## Requirements
1.  **Architecture**:
    - Parent: `BasicScanner`.
    - Child: `MRIScanner`.
2.  **Implementation**:
    - `BasicScanner.__init__` handles `model_name`.
    - `MRIScanner.__init__` handles `model_name` and `tesla_rating`.
    - Use `super()` in the child constructor.
3.  **Validation**:
    - Print the full specs of the MRI scanner.

## Expected Output
```text
Scanner: Siemens Healthineers
Field Strength: 3.0T
```
