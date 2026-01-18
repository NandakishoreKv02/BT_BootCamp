---
title: "The String-to-Patient Factory"
type: app_lab
module: thinking_in_objects
unit: unit_2_14_static_members
lab_number: 4
difficulty: intermediate
use_case: classmethod-factories
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["classmethod", "factory-pattern", "object-creation"]
---

# Lab 4: The String-to-Patient Factory

**Module**: Thinking in Objects
**Objective**: Implement a class method that acts as an alternative constructor to create objects from raw string data.
**Difficulty**: Intermediate
**Context**: Data Migration

## Problem Statement
A hospital is migrating data from a legacy system. The data arrives as raw strings in the format `"Full Name | Age | Blood Type"`. You need to create a `Patient` class that can be initialized normally, but also has a "Factory" method to handle these raw strings.

## Requirements
1.  **Architecture**:
    - Class `Patient`.
2.  **Implementation**:
    - `@classmethod from_legacy_string(cls, data_line)`:
      - Split the string by `" | "`.
      - Return a new instance using `cls(...)`.
3.  **Instantiation**:
    - Create one patient manually.
    - Create one patient using the factory method.

## Expected Output
```text
Manual Patient: Alice (30)
Legacy Patient: Bob (45) - Blood: O+
```
