---
title: "The Clinician Multi-Level Tree"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 5
difficulty: advanced
use_case: complex-inheritance-chain
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["multi-level-inheritance", "super-chains", "specialization"]
---

# Lab 5: The Clinician Multi-Level Tree

**Module**: Thinking in Objects
**Objective**: Build a multi-level inheritance hierarchy and manage attribute propagation through the chain using `super()`.
**Difficulty**: Advanced
**Context**: Professional Staffing

## Problem Statement
A hospital has a complex staffing hierarchy:
1.  **Level 1**: `StaffMember` (Attributes: `name`)
2.  **Level 2**: `Doctor` (Inherits from `StaffMember`. Adds: `license_id`)
3.  **Level 3**: `Surgeon` (Inherits from `Doctor`. Adds: `surgical_specialty`)

You must implement this 3-level tree, ensuring that when a `Surgeon` is initialized, all parent attributes are correctly set via the `super()` chain.

## Requirements
1.  **Architecture**:
    - 3-level chain: `StaffMember` -> `Doctor` -> `Surgeon`.
2.  **Implementation**:
    - Each level's `__init__` must use `super()` to pass data up the chain.
3.  **Validation**:
    - Instantiate a `Surgeon` and print their Name, License, and Specialty.

## Expected Output
```text
Surgeon Profile:
Name: Dr. Gregory House
License: LIC-777
Specialty: Diagnostic Surgery
```
