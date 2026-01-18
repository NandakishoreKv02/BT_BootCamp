---
title: "The Professional Standards Auditor"
type: app_lab
module: thinking_in_objects
unit: unit_2_9_representing_classes
lab_number: 4
difficulty: intermediate
use_case: naming-standards
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["pep-8", "refactoring", "syntax"]
---

# Lab 4: The Professional Standards Auditor

**Module**: Thinking in Objects
**Objective**: Identify and refactor a messy class into a PEP 8 compliant, professional Python blueprint.
**Difficulty**: Intermediate
**Context**: Code Review

## Problem Statement
You have been handed a script for a `surgical_robot` control system. The code works, but it looks like Java/C++ mixed with messy Python. It violates PascalCase and snake_case rules. Your job is to refactor it.

## Requirements
1.  **Refactoring Map**:
    - `surgical_robot` (Class) -> `SurgicalRobot`
    - `RobotID` (attr) -> `robot_id`
    - `PerformCalibration` (method) -> `perform_calibration`
2.  **Implementation**:
    - Build the refactored class.
    - Ensure `self` is used correctly in the method.

## Expected Output
```text
Calibration starting for Robot: R-9
System Ready.
```
