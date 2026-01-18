---
title: "Managing Multiple Instances"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 4
difficulty: intermediate
use_case: hospital_ward
domain: healthcare
order: 4
duration_hours: 0.5
tags:
  topics: ["multiple instances", "objects in lists"]
  subtopics:
    - iteration
    - attribute access
---

# Lab 4: Managing Multiple Instances

**Module**: OOP
**Objective**: Learn how to store and manage multiple objects in a collection like a list.
**Difficulty**: Intermediate
**Context**: Ward Management

## Scenario
You are managing a small hospital ward with 4 beds. You need to create a list of `Patient` objects representing the current residents of the ward and iterate through them to print a census report.

## Goals
- Create 4 distinct `Patient` instances.
- Store these instances in a list called `ward_census`.
- Iterate through the list and print each patient's details.

## Success Criteria
- A list `ward_census` must contain 4 `Patient` objects.
- Each object in the list must have a unique `name` and `condition` attribute.
