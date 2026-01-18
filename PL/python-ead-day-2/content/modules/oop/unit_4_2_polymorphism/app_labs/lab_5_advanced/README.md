---
title: "History & Trends - Collection Protocol"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 5
difficulty: advanced
use_case: medical_device_interface
domain: healthcare
order: 5
duration_hours: 2.0
tags:
  topics: ["oop", "polymorphism", "dunder-methods"]
  subtopics:
    - collection-protocol
    - subtraction-overloading
    - container-emulation
---

# Lab 5: History & Trends - Collection Protocol

**Objective**: Implement container and mathematical dunder methods to allow medical history objects to behave like Python collections and support calculations.

## Generic Information
**Problem Statement**: We have a `VitalHistory` object that stores multiple readings. We want to be able to check its length (`len(history)`), access specific readings (`history[0]`), and subtract two histories to find the difference in averages.
**Goals**:
- Implement `__len__`, `__getitem__`, and `__iter__` to support collection behavior.
- Implement `__sub__` to calculate the difference between the average values of two histories.
- Ensure the object is polymorphic with standard Python lists.

## Use Case: Vital Trends
- **VitalHistory**: Internal list of float values.
- **Access**: Square bracket notation to get a reading at an index.
- **Math**: `history_today - history_yesterday` returns the change in the average vitals.

## Lab Structure
1.  **VitalHistory Class**: Wraps a list of readings.
2.  **Collection Protocol**: Implement indexing and length.
3.  **Operator Overloading**: Implement subtraction between two `VitalHistory` instances.
