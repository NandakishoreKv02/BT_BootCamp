---
title: "The Vitals Refinement"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 4
difficulty: intermediate
use_case: class-refinement
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["composition", "modeling", "refinement"]
---

# Lab 4: The Vitals Refinement

**Module**: Thinking in Objects
**Objective**: Learn to recognize when a simple data attribute has grown complex enough to deserve its own Class.
**Difficulty**: Intermediate
**Context**: Clinical Monitoring

## Problem Statement
A `Patient` object currently has an attribute `vital_signs` which is just a list: `[120, 80, 98.6]`. This is poor design because you can't tell what the numbers mean, and there is no way to validate them.

Your task is to refine this model by creating a dedicated `Vitals` class. The `Patient` will then store a `Vitals` **Object** instead of a raw list.

## Requirements
1.  **Modeling Refinement**:
    - Identify that "Vitals" is a complex noun with its own properties and logic.
2.  **Implementation**:
    - Create a `Vitals` class with `bp_sys`, `bp_dia`, and `temp`.
    - Add a method `is_fever(self)` that returns `True` if temp > 100.4.
    - Update the `Patient` class to hold a `Vitals` object.

## Expected Output
```text
Patient: John Doe
Temp: 101.5 (FEVER DETECTED)
```
