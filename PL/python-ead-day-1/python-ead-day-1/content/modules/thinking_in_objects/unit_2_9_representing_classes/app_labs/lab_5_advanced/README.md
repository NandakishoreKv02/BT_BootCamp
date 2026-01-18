---
title: "The Distributed Clinical Registry"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 5
difficulty: advanced
use_case: object-collections
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["instantiation", "collections", "state-management"]
---

# Lab 5: The Distributed Clinical Registry

**Module**: Thinking in Objects
**Objective**: manage a dynamic collection of objects, ensuring unique state across many instances.
**Difficulty**: Advanced
**Context**: Regional EHR

## Problem Statement
You are building a registry for a hospital network. You need to create a list of `Physician` objects dynamically. Every physician must have a unique ID, a name, and a list of `assigned_patients` which is initially empty.

## Requirements
1.  **Modeling**:
    - Class `Physician`.
2.  **Implementation**:
    - Constructor: `__init__(self, dr_id, name)`.
    - Attribute: `self.assigned_patients = []`.
3.  **The Loop**:
    - Create a range of 5 physicians using placeholders like "Dr. 1", "Dr. 2", etc.
    - Demonstrate that adding a patient to "Dr. 1" DOES NOT add them to "Dr. 2" (Independent lists).

## Expected Output
```text
Creating Registry...
Total Specialists: 5
Dr. 1 Patients: ['Patient A']
Dr. 2 Patients: []
```
