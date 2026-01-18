---
title: "The Patient State Tracker"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 1
difficulty: easy
use_case: instance-attributes
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["attributes", "state", "instance"]
---

# Lab 1: The Patient State Tracker

**Module**: Thinking in Objects
**Objective**: identify and implement **Instance Attributes** that represent the unique clinical state of a patient.
**Difficulty**: Easy
**Context**: ER Admission

## Problem Statement
A triage department needs to track individual patient vitals. Every patient has their own unique heart rate, blood pressure, and oxygen level.

Your task is to create a `PatientState` class that uses instance attributes (`self.`) to store these unique values.

## Requirements
1.  **Attribute Identification**:
    - Instance Attributes: `patient_id`, `hr` (heart rate), `temp`.
2.  **Implementation**:
    - Create the class with an `__init__` method.
3.  **Independence Check**:
    - Create two patient objects and prove that updating the heart rate for Patient A does not affect Patient B.

## Expected Output
```text
Patient 1: HR=72
Patient 2: HR=85
(Verifying independence...)
```
