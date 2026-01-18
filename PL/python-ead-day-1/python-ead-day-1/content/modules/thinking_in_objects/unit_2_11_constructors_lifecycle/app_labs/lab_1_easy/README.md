---
title: "The Simple Admissions Desk"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 1
difficulty: easy
use_case: parameterized-constructor
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["constructor", "initialization", "state"]
---

# Lab 1: The Simple Admissions Desk

**Module**: Thinking in Objects
**Objective**: Implement a parameterized constructor that initializes an object with mandatory data.
**Difficulty**: Easy
**Context**: Patient Triage

## Problem Statement
When a patient arrives at the clinic, a digital `TriageRecord` needs to be created. Every record must contain the patient's name and their primary symptom.

## Requirements
1.  **Architecture**:
    - Class `TriageRecord`.
2.  **Implementation**:
    - Build a constructor that accepts `patient_name` and `symptom`.
    - Store these values as instance attributes.
3.  **Instantiation**:
    - Create a record for "Alice" with "Fever".

## Expected Output
```text
Triage Log Created: Alice [Symptom: Fever]
```
