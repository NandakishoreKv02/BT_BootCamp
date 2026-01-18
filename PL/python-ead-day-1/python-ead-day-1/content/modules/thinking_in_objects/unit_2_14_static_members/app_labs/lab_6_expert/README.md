---
title: "The Universal Staff Factory"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 6
difficulty: expert
use_case: classmethod-inheritance-registry
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["classmethod", "inheritance", "static-registry", "factory-pattern"]
---

# Lab 6: The Universal Staff Factory

**Module**: Thinking in Objects
**Objective**: Build a robust factory method that supports inheritance and tracks all created objects in a static registry list.
**Difficulty**: Expert
**Context**: Human Capital Management

## Problem Statement
A medical group needs a central `StaffRegistry`. 
1.  **Shared Registry**: Every staff member created (Doctors, Nurses, Technicians) must be automatically added to a static list `ALL_STAFF`.
2.  **Flexible Factory**: Implement a `@classmethod` called `spawn_from_name`. This method must use `cls()` to ensure that if called on a subclass (like `Physician`), it returns the correct subtype.

## Requirements
1.  **Architecture**:
    - Base: `MedicalStaff`.
    - Child: `Physician`.
2.  **Implementation**:
    - Static variable `ALL_STAFF = []`.
    - `@classmethod spawn_from_name(cls, name)`:
      - Returns `cls(name)`.
    - In `__init__`:
      - Append `self` to the static list.
3.  **Validation**:
    - Create a generic staff member and a physician using the factory.
    - Verify that both are in the `ALL_STAFF` list.

## Expected Output
```text
Registry Status: 2 Members found.
- [MedicalStaff] General Admin
- [Physician] Dr. Smith
```
