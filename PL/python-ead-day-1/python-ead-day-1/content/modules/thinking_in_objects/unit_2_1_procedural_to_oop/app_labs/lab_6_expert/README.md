---
title: "The Procedural Nightmare"
type: app_lab
module: thinking_in_objects
unit: unit_2_1_procedural_to_oop
lab_number: 6
difficulty: expert
use_case: refactoring
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["refactoring", "architecture", "data-modeling"]
---

# Lab 6: The Hospital Legacy Refactor

**Module**: Thinking in Objects
**Objective**: Transform a fragmented, global-state clinical system into a cohesive, entity-based architecture using structural Object-Oriented principles.
**Difficulty**: Expert
**Context**: Hospital Management

## Problem Statement
The starter code manages a hospital but uses global lists: `patient_names`, `patient_statuses`, `doctor_names`, `doctor_assignments`.
If we want to find which doctor is assigned to a patient, we have to cross-reference indices. It is fragile and unscalable.

## Requirements
1.  **Analyze**: Understand how the current mess works.
2.  **Model**: Design dictionary structures for `Patient` and `Doctor`.
3.  **Refactor**:
    - `create_patient(...)`
    - `create_doctor(...)`
    - `assign_doctor(doctor, patient)` => Updates specific dicts.
    - `discharge_patient(patient)` => Updates status.
4.  **Preserve Logic**: The system must still accurately track who is assigned to whom.

## Expected Output
Same functionality, but cleaner code structure.
```text
Patient 'John' assigned to Dr. House.
Patient 'John' discharged.
```
