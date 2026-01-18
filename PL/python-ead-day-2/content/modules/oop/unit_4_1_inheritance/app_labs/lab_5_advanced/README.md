---
title: "Medical Procedures - Standardization"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 5
difficulty: advanced
use_case: medical_procedures
domain: healthcare
order: 5
duration_hours: 2.5
tags:
  topics: ["oop", "inheritance", "abc"]
  subtopics:
    - abstract-base-classes
    - interface-enforcement
    - concrete-implementations
---

# Lab 5: Medical Procedures - Standardization

**Objective**: Use Abstract Base Classes (ABCs) to enforce a strict interface for all medical procedures.

## Generic Information
**Problem Statement**: The hospital performs many procedures (Surgery, Checkups, X-Rays). All must be loggable and have a duration, but the implementation differs.
**Goals**:
- Define an abstract base class `MedicalProcedure`.
- Enforce implementation of `perform()` and `get_duration()` methods.
- Implement concrete classes `Surgery` and `Checkup`.

## Use Case: Procedures
- **MedicalProcedure (Abstract)**: Cannot be instantiated. Requires `perform()` and `get_duration()`.
- **Surgery**: `perform()` -> "Operating...", `get_duration()` -> 60 mins.
- **Checkup**: `perform()` -> "Checking vitals...", `get_duration()` -> 15 mins.

## Lab Structure
1.  **ABC Definition**: Inherit from `ABC`. Use `@abstractmethod`.
2.  **Concrete Implementations**: Implement required methods.
3.  **Validation**: Try to instantiate the ABC (should fail).
