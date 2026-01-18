---
title: "The Clinical Workflow Modeler"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 6
difficulty: expert
use_case: complex-modeling
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["workflow", "modular-design", "modeling"]
---

# Lab 6: The Clinical Workflow Modeler

**Module**: Thinking in Objects
**Objective**: perform a complete system analysis on a complex clinical narrative. You must identify Entities, Controllers, and Boundries, then implement them as a collaborating ecosystem of classes.
**Difficulty**: Expert
**Context**: End-to-End EHR Simulation

## Problem Statement
The hospital board has provided a "Story" of how the new outpatient surgery center should work:
*"A **Surgeon** plans a **Procedure** for a **Patient**. When the patient arrives, a **Receptionist** marks them as **CheckedIn**. The **OperatingRoom** is reserved for that procedure. After the surgery, the system generates an **InsuranceClaim**."*

In this expert lab, you are the Architect. You must transform this story into a software model.

## Requirements
1.  **System Analysis**:
    - Identify at least 4 Entity classes.
    - Identify at least 1 Controller class to manage the "Reserve Room" or "Plan Procedure" logic.
2.  **Implementation**:
    - Every class must have appropriate attributes.
    - Implement a `HospitalWorkflow` controller that orchestrates the journey.
3.  **Validation**:
    - Ensure that an insurance claim cannot be generated until the patient is marked as "CheckedIn".

## Expected Output
```text
PLANNING: Dr. Strange scheduling Appendectomy for Patient Tony.
OR RESERVED: Operating Room 5 is ready.
CLAIM CREATED: Claim for Tony generated for $5000.
```
