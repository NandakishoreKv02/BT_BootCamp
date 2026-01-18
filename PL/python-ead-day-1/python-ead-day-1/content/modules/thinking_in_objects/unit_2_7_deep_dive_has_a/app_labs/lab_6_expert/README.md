---
title: "The Clinical Ecosystem Architect"
type: app_lab
module: thinking_in_objects
unit: unit_2_7_deep_dive_has_a
lab_number: 6
difficulty: expert
use_case: complex-ecosystem-hierarchy
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["multiplicity", "composition", "aggregation", "ecosystem"]
---

# Lab 6: The Clinical Ecosystem Architect

**Module**: Thinking in Objects
**Objective**: Build a multi-layered ecosystem that enforces different multiplicities and lifecycle rules across three tiers of clinical objects.
**Difficulty**: Expert
**Context**: Enterprise Health Platform

## Problem Statement
You are architecting a health platform. Your system must represent the following:
1.  **Tier 1 (Multi-Patient Ownership)**: A `Clinic` strictly owns multiple `Patient` objects. (1:N Composition).
2.  **Tier 2 (Medication Lifecycle)**: Each `Patient` strictly owns multiple `Medication` objects in their chart. (1:N Composition).
3.  **Tier 3 (Shared Medical Care)**: `Doctor` objects are associated with many `Patient` objects across different clinics. (M:N Aggregation).

## Requirements
1.  **Strict Lifecycle**: If a `Clinic` is deleted, its patients and their medications should logically cease to exist in that context.
2.  **Shared Network**: If a `Clinic` closes, the `Doctor` objects associated with it must continue to exist.
3.  **Implementation**:
    - Build a method `add_patient(self, name)` in `Clinic` that creates the patient internally.
    - Build a method `add_medication(self, drug)` in `Patient` that creates the medication internally.
    - Build a sync method for the Doctor-Patient M:N aggregation.

## Expected Output
```text
CLINIC: City General
  PATIENT: John Doe
    RX: Aspirin
    RX: Insulin
  PHYSICIAN: Dr. House (Shared)
```
