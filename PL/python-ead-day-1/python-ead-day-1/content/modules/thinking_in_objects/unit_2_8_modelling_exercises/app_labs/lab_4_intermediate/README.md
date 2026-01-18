---
title: "Lab Results Pipeline"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 4
difficulty: intermediate
use_case: dependency-modelling
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["dependency", "uses", "refinement"]
---

# Lab 4: Lab Results Pipeline

**Module**: Thinking in Objects
**Objective**: Model a workflow where objects interact as tools without owning each other (**Dependency**).
**Difficulty**: Intermediate
**Context**: Clinical Laboratory

## Problem Statement
A `BloodSample` exists as a data entity. An `Analyzer` is a machine. The machine "uses" the sample to produce a `LabResult`.
1.  **Dependency**: The `Analyzer` does not "have" a sample permanently. It receives it in a method.
2.  **Refinement**: Instead of the Analyzer just printing text, it should return a new `LabResult` object.

## Requirements
1.  **Architecture**:
    - `BloodSample` (sample_id, type).
    - `LabResult` (value, status).
    - `Analyzer` (model_name).
2.  **Implementation**:
    - `Analyzer.process(self, sample_obj)`:
      - Takes a sample.
      - Returns a new `LabResult` object with a value of "Normal" and status "Verified".

## Expected Output
```text
Analyzer: Siemens 500 processing Sample-X
Result: Normal (Status: Verified)
```
