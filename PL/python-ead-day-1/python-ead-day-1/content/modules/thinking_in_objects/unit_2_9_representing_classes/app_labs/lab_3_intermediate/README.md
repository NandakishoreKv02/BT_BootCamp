---
title: "The Pharmacy Fulfiller"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 3
difficulty: intermediate
use_case: method-interaction
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["methods", "self-calling", "instantiation"]
---

# Lab 3: The Pharmacy Fulfiller

**Module**: Thinking in Objects
**Objective**: Practice calling methods from both inside the class (using `self`) and from outside (using the object name).
**Difficulty**: Intermediate
**Context**: Inpatient Pharmacy

## Problem Statement
A `Prescription` needs to be processed. 
1.  **Stage 1: Validate**: Check if the dosage is within range.
2.  **Stage 2: Fulfill**: If valid, mark as "Filled". 

The "Fulfill" method should call the "Validate" method internally before proceeding.

## Requirements
1.  **Architecture**:
    - Class `Prescription`.
2.  **Implementation**:
    - `validate(self)`: Returns `True` if `dosage <= 100`.
    - `fulfill(self)`: 
      - Calls `self.validate()`.
      - If valid, sets `self.status = "Filled"`.
3.  **Validation**:
    - Instantiate a prescription and call `.fulfill()`.

## Expected Output
```text
Validating dosage: 50mg...
Prescription Fulfilling...
Status: Filled
```
