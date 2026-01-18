---
title: "Instance vs Class Variables"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 3
difficulty: intermediate
use_case: patient_counter
domain: healthcare
order: 3
duration_hours: 0.5
tags:
  topics: ["class variables", "instance variables"]
  subtopics:
    - shared state
    - object state
---

# Lab 3: Instance vs Class Variables

**Module**: OOP
**Objective**: Differentiate between variables specific to an instance and variables shared by all instances.
**Difficulty**: Intermediate
**Context**: Tracking Total Patient Admissions

## Scenario
The clinic manager wants to know how many patients have been admitted in total. You need to add a way to track the total number of `Patient` instances created using a **class variable**.

## Goals
- Define a class variable `total_patients`.
- Increment the class variable inside the `__init__` constructor.
- Access both instance variables (`name`) and the class variable.

## Success Criteria
- The class variable `total_patients` should increment every time a new `Patient` is created.
- Each `Patient` instance should still maintain its own unique `name`.
