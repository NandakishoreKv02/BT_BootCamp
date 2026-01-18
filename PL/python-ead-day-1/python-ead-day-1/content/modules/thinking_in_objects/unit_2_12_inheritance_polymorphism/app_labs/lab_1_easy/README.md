---
title: "The Hospital Registry"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 1
difficulty: easy
use_case: basic-inheritance
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["inheritance", "class-hierarchy", "subclassing"]
---

# Lab 1: The Hospital Registry

**Module**: Thinking in Objects
**Objective**: Implement a basic inheritance relationship between a general person and a specific medical staff member.
**Difficulty**: Easy
**Context**: Human Resources

## Problem Statement
A hospital registry needs to track `Person` entities. Every person has a `name`. However, a `StaffMember` is a specific type of person who also has an `employee_id`. You must use inheritance to avoid redefining the `name` attribute in the staff class.

## Requirements
1.  **Modeling**:
    - Parent class `Person`.
    - Child class `StaffMember`.
2.  **Implementation**:
    - `Person` should initialize `name`.
    - `StaffMember` should inherit from `Person` and initialize `employee_id`.
3.  **Instantiation**:
    - Create a `StaffMember` named "John Smith" with ID "EMP-101".

## Expected Output
```text
Staff Name: John Smith
Employee ID: EMP-101
Relationship Check: StaffMember is-a Person: True
```
