---
title: "The Cohesive Lab Report"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 4
difficulty: intermediate
use_case: cohesion-refactoring
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["cohesion", "refactoring", "class-design"]
---

# Lab 4: The Cohesive Lab Report

**Module**: Thinking in Objects
**Objective**: refactor a low-cohesion class into a **Highly Cohesive** one by separating clinical logic from administrative tasks.
**Difficulty**: Intermediate
**Context**: Laboratory Information System (LIS)

## Problem Statement
A `LabReport` class currently contains methods for analyzing blood results, AND methods for processing social media notifications for the hospital. This is **Low Cohesion**. A report object should only care about medical data.

Your task is to identify and remove the non-cohesive methods, and ensure the remaining methods work together to represent a single medical entity.

## Requirements
1.  **Audit**:
    - Identify methods that don't belong in a `LabReport` (e.g., `post_to_twitter`).
2.  **Implementation**:
    - Implement a cohesive `LabReport` class with attributes like `patient_id` and `test_results` (a dictionary).
    - Add a method `get_status()` that returns "Abnormal" if any result is outside a range.
3.  **Refactoring**:
    - Demonstrate that the class is now focused entirely on the lab result.

## Expected Output
```text
Lab Report for Patient 505:
Results: {'Glucose': 140}
Status: Abnormal
```
