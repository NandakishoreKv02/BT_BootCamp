---
title: "The Appointment Book"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 3
difficulty: intermediate
use_case: multiplicity-modelling
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["composition", "aggregation", "multiplicity"]
---

# Lab 3: The Appointment Book

**Module**: Thinking in Objects
**Objective**: Model a complex clinical schedule using various multiplicities.
**Difficulty**: Intermediate
**Context**: Clinic Operations

## Problem Statement
A `DailySchedule` is a high-level container for appointments.
1.  **1:N Composition**: A `DailySchedule` owns multiple `TimeSlot` objects.
2.  **Aggregation (Link)**: Each `TimeSlot` is associated with one `Patient` and one `Physician`.

## Requirements
1.  **Architecture**:
    - Build `Physician` and `Patient` classes.
    - Build `TimeSlot` class.
    - Build `DailySchedule` class.
2.  **Implementation**:
    - The `DailySchedule` should initialize its list of `TimeSlot` objects (e.g., 9:00, 10:00, 11:00).
    - It should have a method `book_slot(self, slot_time, patient, doctor)` to link the objects.

## Expected Output
```text
Schedule for 2026-05-10:
[9:00]: Alice with Dr. House
[10:00]: Open
```
