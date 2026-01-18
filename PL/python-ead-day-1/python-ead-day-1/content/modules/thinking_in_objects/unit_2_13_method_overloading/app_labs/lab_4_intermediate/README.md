---
title: "The Dynamic Patient Tagger"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 4
difficulty: intermediate
use_case: kwargs-keyword-arguments
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["kwargs", "keyword-arguments", "dynamic-metadata"]
---

# Lab 4: The Dynamic Patient Tagger

**Module**: Thinking in Objects
**Objective**: Implement a method that uses `**kwargs` to accept an arbitrary number of named clinical flags or metadata tags.
**Difficulty**: Intermediate
**Context**: Medical Informatics

## Problem Statement
A `PatientProfile` needs a method `add_tags` that allows staff to attach any amount of metadata (e.g., `smoker=True`, `allergy="Peanuts"`, `last_visit="2023-10-01"`). You must use `**kwargs` to capture these into an internal dictionary.

## Requirements
1.  **Modeling**:
    - Class `PatientProfile` with a `name` and a `tags` dictionary.
2.  **Implementation**:
    - `add_tags(self, **kwargs)`:
      - Update the internal `self.tags` dictionary with everything in `kwargs`.
3.  **Instantiation**:
    - Create a profile and add at least 3 distinct tags using keyword arguments.

## Expected Output
```text
Patient: John Doe
Tags Attached:
- smoker: True
- allergy: Peanuts
- risk_level: High
```
