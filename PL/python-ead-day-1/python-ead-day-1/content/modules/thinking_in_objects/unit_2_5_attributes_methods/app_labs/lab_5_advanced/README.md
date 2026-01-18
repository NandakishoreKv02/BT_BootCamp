---
title: "The Equipment Maintenance Hub"
type: app_lab
module: thinking_in_objects
unit: unit_2_5_attributes_methods
lab_number: 5
difficulty: advanced
use_case: class-vs-instance-mutation
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["class-attributes", "instance-attributes", "lifecycles"]
---

# Lab 5: The Equipment Maintenance Hub

**Module**: Thinking in Objects
**Objective**: manage complex object state by balancing **Class Attributes** (institutional standards) and **Instance Attributes** (specific device wear and tear).
**Difficulty**: Advanced
**Context**: Biomedical Engineering

## Problem Statement
A hospital's biomedical department maintains thousands of devices. Every `Ventilator` has its own `operating_hours`. However, the entire hospital follows a single `SERVICE_THRESHOLD` (e.g., service is required after every 1000 hours).

You need to build an asset tracker where:
1.  Changing the `SERVICE_THRESHOLD` in one place affects all ventilators.
2.  Each ventilator tracks its own hours independently.

## Requirements
1.  **Attribute Design**:
    - Class Attribute: `service_threshold = 1000`.
    - Instance Attribute: `hours_run`.
2.  **Implementation**:
    - Method `add_hours(self, amount)`: Increases instance hours.
    - Method `needs_service(self)`: Returns `True` if `hours_run >= service_threshold`.
3.  **Global Update**:
    - In `main`, simulate a hospital policy change where the threshold is reduced to 800 hours for all devices.

## Expected Output
```text
Device 1: 900 hours. Service Needed? False
--- Policy Change: 800 Hours ---
Device 1: 900 hours. Service Needed? True
```
