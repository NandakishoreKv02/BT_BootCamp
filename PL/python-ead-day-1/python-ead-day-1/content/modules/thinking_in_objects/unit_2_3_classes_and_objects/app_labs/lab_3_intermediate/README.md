---
title: "The Intelligent BP Monitor"
type: app_lab
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
lab_number: 3
difficulty: intermediate
use_case: behavior-methods
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["methods", "self", "state-mutation"]
---

# Lab 3: The Intelligent BP Monitor

**Module**: Thinking in Objects
**Objective**: move beyond simple data storage by adding **Behavior** (Methods) to your class.
**Difficulty**: Intermediate
**Context**: Intensive Care Unit (Monitoring)

## Problem Statement
A blood pressure (BP) monitor doesn't just store numbers; it analyzes them. We need a `BPMonitor` class that can take a reading and decide if the pressure is "High", "Low", or "Normal".

## Requirements
1.  **Class Design**:
    - `__init__(self, patient_name)`: Stores the name and initializes `systolic` and `diastolic` to 0.
2.  **State Mutation**:
    - `take_reading(self, sys, dia)`: Updates the systolic and diastolic attributes.
3.  **Complex Behavior**:
    - `get_analysis(self)`: Returns "Hypertension" if systolic > 140, "Hypotension" if systolic < 90, else "Normal".

## Expected Output
```text
Reading for John Doe...
Status: Hypertension (150/95)
```
