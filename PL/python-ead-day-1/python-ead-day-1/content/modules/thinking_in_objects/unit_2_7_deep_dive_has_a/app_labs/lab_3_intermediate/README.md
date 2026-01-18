---
title: "The Bidirectional Care Link"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 3
difficulty: intermediate
use_case: bidirectional-association
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["navigability", "bidirectional", "multiplicity"]
---

# Lab 3: The Bidirectional Care Link

**Module**: Thinking in Objects
**Objective**: Implement a **Bidirectional Association** with 1:N multiplicity, ensuring that both objects stay in sync.
**Difficulty**: Intermediate
**Context**: Primary Care

## Problem Statement
In a clinic, a `Doctor` has many `Patient` objects. To make the system efficient, we want **bidirectional navigability**:
1.  The doctor should be able to list all their patients.
2.  The patient should be able to identify their assigned doctor.

## Requirements
1.  **Modeling**:
    - `Doctor` class (list of patients).
    - `Patient` class (`doctor` attribute).
2.  **Sync Logic**:
    - When a patient is added to a doctor's list, the patient's `doctor` attribute must be updated to point back to that doctor.
3.  **Validation**:
    - Assign a patient to a doctor and prove that `p.doctor == dr` and `p in dr.patients`.

## Expected Output
```text
Assigning Patient John to Dr. Smith...
John's records show Dr. Smith as primary.
Dr. Smith's list contains: ['John']
```
