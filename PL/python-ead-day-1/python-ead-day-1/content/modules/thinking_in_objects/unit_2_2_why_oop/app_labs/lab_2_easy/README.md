---
title: "Common Clinical Logger"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 2
difficulty: easy
use_case: reusability
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["reusability", "logging", "dry-principle"]
---

# Lab 2: Common Clinical Logger

**Module**: Thinking in Objects
**Objective**: Demonstrate **Reusability** by creating a single Logger utility that provides standardized audit trails for multiple independent departments.
**Difficulty**: Easy
**Context**: Regulatory Compliance (Audit Trails)

## Problem Statement
Every action in a hospital must be logged for regulatory compliance. Currently, the Pharmacy team and the Admission team have written their own separate `print` statements. This duplication makes it impossible to standardize the audit format across the whole hospital.

Your task is to create a reusable `Logger` object that can be "plugged into" any department, ensuring all clinical events follow the same format.

## Requirements
1.  **Shared Logic**: Create a `make_logger(service_name)` function that initializes a standardized logger dictionary.
2.  **Centralized Behavior**: Define a `log_event(logger, message)` function that handles the formatting for any service.
3.  **DRY (Don't Repeat Yourself)**: Use the same `log_event` logic for both Pharmacy and Admissions departments.

## Expected Output
```text
[PHARMACY]: Administered Aspirin
[ADMISSIONS]: Admitted John Doe
[PHARMACY]: Stock updated: Amoxicillin +50
```
(Notice how the format is identical because both services share the same object logic.)
