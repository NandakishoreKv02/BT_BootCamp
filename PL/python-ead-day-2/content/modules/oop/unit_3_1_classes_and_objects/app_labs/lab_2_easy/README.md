---
title: "The Constructor and Self"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 2
difficulty: easy
use_case: patient_details
domain: healthcare
order: 2
duration_hours: 0.5
tags:
  topics: ["constructor", "self"]
  subtopics:
    - __init__
    - instance initialization
---

# Lab 2: The Constructor and Self

**Module**: OOP
**Objective**: Understand how to use the `__init__` method to initialize object state.
**Difficulty**: Easy
**Context**: Initializing Patient Records

## Scenario
In Lab 1, your `Patient` class didn't store any information. Now, you need to update it so that every time a new `Patient` object is created, it stores the patient's name and age.

## Goals
- Implement the `__init__` method.
- Use the `self` parameter to assign attributes.
- Initialize `name` and `age` attributes.

## Success Criteria
- The `Patient` class should have an `__init__` method.
- The constructor should accept `name` and `age`.
- Instances created with specific values should store those values correctly.
