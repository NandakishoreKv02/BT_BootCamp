---
title: "Hospital Ward Manager"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 3
difficulty: advanced
use_case: hospital_ward_management
domain: healthcare
order: 3
duration_hours: 4.5
tags:
  topics: ["oop", "methods"]
  subtopics:
    - method-coordination
    - side-effects
    - return-values
    - static-methods
    - class-methods
---

# Lab 3: Hospital Ward Manager

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master the coordination of instance, class, and static methods in a complex system.
**Difficulty**: Advanced
**Context**: Hospital Inpatient Operations

## Generic Information
**Problem Statement**: Managing a hospital ward requires more than just storing patient names. We need to track the total occupancy across the entire hospital (class state), perform medical calculations (static logic), and update individual patient status (instance state) while returning meaningful feedback.
**Goals**:
- Coordinate multiple method types to solve a multi-layered problem.
- Practice "Command-Query Separation" (differentiating side effects from return values).
- Implement professional-grade error handling and auditing.
**Data Elements**:
- `Patient.total_patients`: Class-level counter.
- `inventory`: Instance-level list of medications.
- `HealthUtils`: Static methods for dosing logic.

## Use Case
**Title**: Admission and Treatment Workflow
**Description**: When a patient is admitted, the hospital-wide count must increase. During treatment, a medication is dispensed (side effect), and a dosage report is generated (return value).

### Rules
- Discharging a patient should never allow the total count to drop below zero.
- Dosing calculations must be validated before dispensing medication.
- Methods should return boolean success/failure alongside performing actions.

### Test Cases
- Case 1: Admit 3 patients and verify total count is 3.
- Case 2: Dispense medication only if sufficient stock exists.
- Case 3: Calculate BMI using a static method and verify its use in dosage logic.

### Success Criteria
- Global counter is accurate across all instances.
- Inventory is properly decremented (side effect).
- Correct dosage is returned based on patient weight (return value).

## Overview
This advanced lab represents a production-grade component. You will see how the different method types "talk" to each other to build a robust system.

---
