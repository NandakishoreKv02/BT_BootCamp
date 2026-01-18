---
title: "The Clinical Interaction Simulator"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 6
difficulty: expert
use_case: object-collaboration
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["composition", "object-interaction", "modeling"]
---

# Lab 6: The Clinical Interaction Simulator

**Module**: Thinking in Objects
**Objective**: Build a multi-object system where instances of different classes (Patient, Doctor, Appointment) interact and collaborate to share state.
**Difficulty**: Expert
**Context**: Clinical Operations (EHR)

## Problem Statement
In a real hospital, objects don't exist in isolation. A `Patient` is assigned to a `Doctor`. An `Appointment` links a `Patient`, a `Doctor`, and a `Time`. 

You will build a simulator where:
1.  A `Doctor` can be assigned to multiple `Patients`.
2.  A `Patient` stores a reference to their primary `Doctor`.
3.  Each object can report its status, showing the connections.

## Requirements
1.  **Doctor Class**: `__init__(self, name)` and `self.patients` (list).
2.  **Patient Class**: `__init__(self, name, mrn)` and `self.primary_doctor` (None).
3.  **Interaction Method**: `assign_patient(doctor, patient)`:
    - This function (or method) should update the patient's `primary_doctor` AND add the patient to the doctor's `patients` list.
4.  **Reporting**: A method to print a summary of a doctor's entire patient load.

## Expected Output
```text
Assigning John Doe to Dr. House...
Dr. House's Census:
- John Doe (MRN789)
```
(Notice how updating one object's reference can be linked to the other.)
