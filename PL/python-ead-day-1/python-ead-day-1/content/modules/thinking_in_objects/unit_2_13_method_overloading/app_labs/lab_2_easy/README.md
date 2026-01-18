---
title: "The Multi-Sourced Vital Logger"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 2
difficulty: easy
use_case: positional-argument-handling
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["overloading", "pythonic-logic", "argument-handling"]
---

# Lab 2: The Multi-Sourced Vital Logger

**Module**: Thinking in Objects
**Objective**: Simulate overloading by creating a single method that branches its logic based on which arguments are provided.
**Difficulty**: Easy
**Context**: Intensive Care Monitoring

## Problem Statement
A `VitalLogger` needs to record a heart rate. Sometimes, we only have the `bpm` value. Other times, we have the `bpm` and a `sensor_id`. You must use default arguments to create a method that reacts differently based on whether the sensor ID is present.

## Requirements
1.  **Modeling**:
    - Class `VitalLogger`.
2.  **Implementation**:
    - `log_hr(self, bpm, sensor=None)`:
      - If `sensor` is `None`, return "Logged BPM: {bpm}".
      - If `sensor` is provided, return "Logged BPM: {bpm} from Sensor {sensor}".

## Expected Output
```text
Logged BPM: 72
Logged BPM: 85 from Sensor S-99
```
