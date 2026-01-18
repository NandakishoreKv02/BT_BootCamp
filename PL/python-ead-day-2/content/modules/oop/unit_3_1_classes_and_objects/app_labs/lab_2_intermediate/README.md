---
title: "Clinical Vitals Tracker"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 2
difficulty: intermediate
use_case: vitals_monitoring
domain: healthcare
order: 2
duration_hours: 2
tags:
  topics: ["oop", "methods"]
  subtopics:
    - instance-methods
    - state-management
    - self-parameter
    - behavior-encapsulation
---

# Lab 2: Clinical Vitals Tracker

**Module**: Object-Oriented Programming - Part 1
**Objective**: Implement instance methods to manage object behavior and internal state.
**Difficulty**: Intermediate
**Context**: Patient Monitoring

## Generic Information
**Problem Statement**: Storing patient name and age is a good start, but doctors need to track medical data over time, such as heart rate readings. Objects should be able to "do things" like record a new reading and calculate averages.
**Goals**:
- Add behavior (methods) to the Patient object.
- Manage dynamic state (lists) within an object.
- Use `self` to differentiate between the object's data and local variables.
**Data Elements**:
- `vitals`: A list of heart rate readings (integers).

## Use Case
**Title**: Track Patient Heart Rate
**Description**: A nurse needs to record multiple heart rate readings for a patient during their stay and calculate the average heart rate to check for anomalies.

### Rules
- Heart rate readings must be stored chronologically.
- Calculating the average must handle cases where no vitals have been recorded yet (should return 0).

### Test Cases
- Case 1: Add readings [72, 80, 75] and verify the average is 75.66.
- Case 2: Check average for a new patient with no readings (ensure no crash).

### Success Criteria
- Method `add_vital()` correctly updates the internal list.
- Method `get_average_heart_rate()` returns correct mathematical average.

## Overview
This intermediate lab builds on the previous foundational work. You will transition from seeing objects as "data containers" to seeing them as "intelligent entities" that manage their own state.

## Learning Goals
- Implement instance methods.
- Manage internal list state with `self.attribute.append()`.
- Use conditional logic within methods based on instance data.

## The Scenario
The clinic now uses digital monitors. Instead of manually updating a spreadsheet, the patient object itself should handle the incoming stream of medical data.

## What You'll Build
You will extend the `Patient` class from Lab 1 to include a vitals tracking system.

## How to Use This Lab
1. **Analyze** the new requirements in `tasks.md`.
2. **Implement** the logic in `starter_code.py`.
3. **Run** `tests.py` to verify your implementation.

## Task Summary
- Task 1: Initialize the vitals list.
- Task 2: Implement the `add_vital` method.
- Task 3: Implement the `get_average_heart_rate` method.

## Time Estimate
- Reading & Planning: 15 minutes
- Implementation: 1.5 - 2 hours
- Testing: 15 minutes
- **Total**: ~2.5 hours
---
