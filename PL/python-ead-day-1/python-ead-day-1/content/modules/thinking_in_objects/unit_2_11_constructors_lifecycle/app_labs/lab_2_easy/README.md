---
title: "The Flexible Lab Request"
type: app_lab
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
lab_number: 2
difficulty: easy
use_case: default-parameters
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["default-values", "optional-parameters", "constructor"]
---

# Lab 2: The Flexible Lab Request

**Module**: Thinking in Objects
**Objective**: Use default parameters to handle standard vs. urgent medical requests.
**Difficulty**: Easy
**Context**: Pathology Lab

## Problem Statement
A `LabRequest` typically has a priority of "Routine". However, in some cases, it needs to be "STAT" (Urgent). Your task is to design a class that defaults to Routine but allows the developer to override it.

## Requirements
1.  **Modeling**:
    - Class `LabRequest`.
2.  **Implementation**:
    - Constructor accepts `test_name`.
    - Constructor accepts `priority` with a default value of "Routine".
3.  **Instantiation**:
    - Create a routine "Blood Count" request.
    - Create a STAT "Glucose" request.

## Expected Output
```text
Order: Blood Count | Priority: Routine
Order: Glucose | Priority: STAT
```
