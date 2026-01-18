---
title: "The Lifecycle Auditor"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 4
difficulty: intermediate
use_case: complex-lifecycle
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["lifecycle", "composition", "aggregation"]
---

# Lab 4: The Lifecycle Auditor

**Module**: Thinking in Objects
**Objective**: Differentiate between **Composition** (strong ownership) and **Aggregation** (shared association) by implementing a class that manages both.
**Difficulty**: Intermediate
**Context**: Medical Records Management

## Problem Statement
A `PatientFile` is the central hub for clinical data. 
1.  **Composition**: Every file MUST have a `MedicalHistory` object created internally when the file is opened. If the file is closed/deleted, the history is gone.
2.  **Aggregation**: A file can be assigned a `ReviewingDoctor`. If the file is deleted, the doctor continues to exist in the global hospital list.

## Requirements
1.  **Structural Design**:
    - `MedicalHistory` (created in `PatientFile.__init__`).
    - `Doctor` (passed into `PatientFile` via a method).
2.  **Implementation**:
    - Build the `PatientFile` class to enforce these two distinct lifecycles.
3.  **Audit**:
    - Demonstrate how the `MedicalHistory` is unique to the file, while the `Doctor` is shared.

## Expected Output
```text
Opening File for Smith...
History Object: <Object_A> created internally.
Assigning Dr. House...
Reviewing Doctor: House
```
