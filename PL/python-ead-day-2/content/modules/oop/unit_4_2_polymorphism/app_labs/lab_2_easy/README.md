---
title: "Device Manager - Inheritance"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 2
difficulty: easy
use_case: medical_device_interface
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["oop", "polymorphism", "inheritance"]
  subtopics:
    - method-overriding
    - polymorphism-via-inheritance
    - state-management
---

# Lab 2: Device Manager - Inheritance

**Objective**: Use inheritance and method overriding to manage device state (start/stop) polymorphically.

## Generic Information
**Problem Statement**: All medical devices need to be started and halted. However, starting an X-Ray machine is different from starting a Heart Rate monitor.
**Goals**:
- Create a base `Device` class with `start()` and `stop()`.
- Create subclasses `XRayMachine` and `HeartMonitor` that override these methods.
- Demonstrate treating both subclasses as `Device` objects.

## Use Case: Device Control
- **Device**: Base behavior (prints "Device starting...").
- **XRayMachine**: "Warming up radiation source...".
- **HeartMonitor**: "Calibrating sensors...".

## Lab Structure
1.  **Base Class**: `Device` with default methods.
2.  **Subclasses**: Override methods with specific strings.
3.  **Manager**: Iterate a list of devices and call `start()`.
