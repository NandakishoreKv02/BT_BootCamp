---
title: "The Pharmacy Dispenser"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 3
difficulty: intermediate
use_case: dependency-uses
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["dependency", "uses", "parameter-passing"]
---

# Lab 3: The Pharmacy Dispenser

**Module**: Thinking in Objects
**Objective**: Implement a **Uses** (Dependency) relationship where one object interacts with another only through a method parameter.
**Difficulty**: Intermediate
**Context**: Inpatient Pharmacy

## Problem Statement
A `MedicationDispenser` machine is a tool. It doesn't "own" a `Patient` or a `Prescription`. It simply **uses** a `Prescription` object to fetch the correct dose and then **uses** a `Patient` object to verify the name before dispensing.

Your task is to implement the dispenser so that it receives its "targets" as method arguments.

## Requirements
1.  **Modeling (Uses)**:
    - `MedicationDispenser` class should have NO instance attributes for patient or drug.
    - It should have a method `dispense(self, patient_obj, rx_obj)`.
2.  **Implementation**:
    - The `dispense` method should print a verification message: "Dispensing [drug] for [patient_name]".
3.  **Validation**:
    - Create the dispenser once, then use it for multiple different patients to prove it is a reusable tool.

## Expected Output
```text
Verifying: John Doe
Action: Dispensing 500mg Aspirin.
```
