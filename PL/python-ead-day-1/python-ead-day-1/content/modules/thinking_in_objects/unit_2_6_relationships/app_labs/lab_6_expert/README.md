---
title: "The Hospital Ecosystem"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 6
difficulty: expert
use_case: complex-ecosystem-modeling
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["inheritance", "composition", "dependency", "aggregation"]
---

# Lab 6: The Hospital Ecosystem

**Module**: Thinking in Objects
**Objective**: Build a complete clinical ecosystem that utilizes every relationship type correctly: **Inheritance**, **Composition**, **Aggregation**, and **Dependency**.
**Difficulty**: Expert
**Context**: Integrated Hospital Management

## Problem Statement
You need to model the interaction between four different entities in a hospital:
1.  **Inheritance (Is-a)**: There are general `ClinicalStaff` and specific `Physicians`.
2.  **Composition (Has-a)**: A `Hospital` is composed of multiple `Ward` objects.
3.  **Aggregation (Link)**: A `Ward` is linked to a `HeadNurse` (the nurse exists even if the ward is empty).
4.  **Dependency (Uses)**: A `Physician` uses an `Analyzer` to check results.

Your task is to implement this integrated web of objects.

## Requirements
1.  **Architecture**:
    - Class `Staff` (base).
    - Class `Physician` (inherits from Staff).
    - Class `Ward` (has a `name` and a `nurse`).
    - Class `Hospital` (creates 2 wards in its `__init__`).
    - Class `Analyzer` (a tool with a `process()` method).
2.  **Interaction**:
    - The `Physician` should have a method `run_lab(self, analyzer_obj, sample_name)`.
3.  **Simulation**:
    - Create a hospital, which creates its wards.
    - Assign a nurse to a ward.
    - Have a physician use an analyzer to process a sample.

## Expected Output
```text
Hospital initialized with 2 wards.
Ward: ICU managed by Nurse Nightingale.
Dr. House processing Blood Sample via Alpha-Analyzer... Result: DONE.
```
