---
title: "Patient Lookup - Specific Errors"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 1
difficulty: easy
use_case: semantic_errors
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["exceptions", "custom-class", "semantic-meaning"]
  subtopics:
    - definition
    - raising
---

# Lab 1: Patient Lookup - Specific Errors

**Objective**: Implement a `PatientNotFound` exception to replace generic `ValueError` or `KeyError`, making the code self-documenting.

## Generic Information
**Problem Statement**: When a user isn't found, returning `None` forces the caller to check for None everywhere. Raising `KeyError` is confusing because it's an implementation detail (using a dict).
**Goals**:
- Define `class PatientNotFound(Exception)`.
- Implement `find_patient(id)`.
- Raise `PatientNotFound` if ID is missing.

## Use Case: Semantic Errors
A "ReceptionDesk" app looks up patients. If the ID is wrong, it should report "Patient ID not found", not "KeyError: '123'".

## Lab Structure
1.  **Custom Exception**: Defining the class.
2.  **Lookup Function**: Using the exception.
3.  **Consumer**: Catching the specific exception.

## Getting Started
Just inherit from `Exception`: `class MyError(Exception): pass`.
