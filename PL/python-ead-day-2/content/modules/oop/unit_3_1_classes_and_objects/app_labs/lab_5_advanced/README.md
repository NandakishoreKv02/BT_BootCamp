---
title: "Object Identity and Equality"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 5
difficulty: advanced
use_case: patient_deduplication
domain: healthcare
order: 5
duration_hours: 0.5
tags:
  topics: ["identity", "equality"]
  subtopics:
    - is operator
    - == operator
    - memory addresses
---

# Lab 5: Object Identity and Equality

**Module**: OOP
**Objective**: Understand the difference between two objects being the same instance (identity) and two objects having the same data (equality).
**Difficulty**: Advanced
**Context**: Patient Record Deduplication

## Scenario
You found two patient records in the system for "John Smith". You need to determine if they are literally the same object in memory or if they are two different objects that just happen to have the same name.

## Goals
- Create two separate objects with identical data.
- Create a third reference to one of the existing objects.
- Use the `is` operator to check identity.
- Use the `==` operator (default behavior vs custom) to check equality.

## Success Criteria
- Identify that two separate objects with the same data are NOT the same object (`is` returns `False`).
- Identify that two references to the same object ARE the same object (`is` returns `True`).
