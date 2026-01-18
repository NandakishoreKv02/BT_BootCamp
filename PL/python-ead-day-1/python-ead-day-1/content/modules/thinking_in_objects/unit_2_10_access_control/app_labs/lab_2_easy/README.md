---
title: "The Heartbeat Guard"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 2
difficulty: easy
use_case: basic-property
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["property-decorator", "getter", "encapsulation"]
---

# Lab 2: The Heartbeat Guard

**Module**: Thinking in Objects
**Objective**: Use the `@property` decorator to create a read-only interface for a medical sensor.
**Difficulty**: Easy
**Context**: Intensive Care

## Problem Statement
A `HeartMonitor` receives pulses from a sensor. We want external users to be able to see the `bpm`, but we DO NOT want them to be able to manually change the bpm from outside the class (which would be fraud or a medical error).

## Requirements
1.  **Modeling**:
    - Class `HeartMonitor`.
2.  **Implementation**:
    - Store the bpm in a protected variable `_bpm`.
    - Create a `@property` named `bpm` that returns this value.
3.  **Validation**:
    - Try to assign a new value to `monitor.bpm = 100`. It should fail with an `AttributeError`.

## Expected Output
```text
Current BPM: 72
(Attempting manual override...)
Error: can't set attribute
```
