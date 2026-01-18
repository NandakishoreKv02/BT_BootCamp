---
title: "The Case ID Generator"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 3
difficulty: intermediate
use_case: class-variable-generation
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["static-variables", "id-generation", "singleton-state"]
---

# Lab 3: The Case ID Generator

**Module**: Thinking in Objects
**Objective**: Use a static class variable to generate unique, sequential ID numbers for new medical cases.
**Difficulty**: Intermediate
**Context**: Clinical Registry

## Problem Statement
A `MedicalCase` object needs a unique `case_id` (e.g., 1001, 1002). Instead of asking the user to provide an ID, the class should "know" what the next ID is. 

## Requirements
1.  **Modeling**:
    - Class `MedicalCase`.
2.  **Implementation**:
    - Static variable `next_id = 1000`.
    - In `__init__`:
      - Increment `MedicalCase.next_id`.
      - Assign the NEW value to `self.case_id`.
3.  **Encapsulation**:
    - Ensure the `case_id` is unique for every instance even if created in different parts of the code.

## Expected Output
```text
New Case: Chest Pain (ID: 1001)
New Case: Sprained Ankle (ID: 1002)
New Case: Routine Check (ID: 1003)
```
