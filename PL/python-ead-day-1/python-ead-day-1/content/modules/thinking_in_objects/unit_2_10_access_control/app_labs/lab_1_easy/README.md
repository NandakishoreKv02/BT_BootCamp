---
title: "The Locked Record"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 1
difficulty: easy
use_case: basic-encapsulation
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["private-members", "naming", "encapsulation"]
---

# Lab 1: The Locked Record

**Module**: Thinking in Objects
**Objective**: Implement basic encapsulation to signal that specific medical identifies should not be touched.
**Difficulty**: Easy
**Context**: Data Privacy

## Problem Statement
A `PatientFile` contains a `social_security` number. This is high-sensitivity data. You must encapsulate it using Python's naming conventions to ensure it doesn't accidentally show up in public attribute lists or get easily modified.

## Requirements
1.  **Architecture**:
    - Class `PatientFile`.
2.  **Implementation**:
    - User single underscore (`_`) for "Protected" data (internal ID).
    - Use double underscore (`__`) for "Private" data (SSN).
3.  **Validation**:
    - Try to print the object's attributes. Notice how the SSN is "hidden" (mangled).

## Expected Output
```text
File Name: John Doe
Protected ID: P-101
(Direct access to SSN should fail or be mangled)
```
