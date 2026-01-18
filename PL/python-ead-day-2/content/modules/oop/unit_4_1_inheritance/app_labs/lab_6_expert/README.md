---
title: "Doctor Scheduling - Composition vs Inheritance"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 6
difficulty: expert
use_case: hospital_scheduling
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["oop", "inheritance", "composition"]
  subtopics:
    - decoupling-logic
    - system-refactoring
    - flexible-shaping
---

# Lab 6: Doctor Scheduling - Composition vs Inheritance

**Objective**: Refactor a rigid inheritance-based design into a flexible composition-based design.

## Generic Information
**Problem Statement**: Originally, the system defined schedules via inheritance: `DayShiftDoctor`, `NightShiftDoctor`, `RotatingShiftDoctor`. This created a combinatorial explosion of classes (e.g., `DayShiftSurgeon`, `NightShiftSurgeon`).
**Goals**:
- Stop using inheritance for scheduling.
- Separate the "Schedule" concept into its own class.
- Give the `Doctor` class a `schedule` attribute (Composition).

## Use Case: Flexible Shifts
- **Schedule Class**: Handles determining if a doctor is available at a given hour.
- **Doctor Class**: *Has a* `Schedule`. Delegates availability checks to it.

## Lab Structure
1.  **Schedule Class**: Logic for checking hours.
2.  **Doctor Class**: Initialized with a `Schedule`.
3.  **Refactoring**: Demonstrate how a `Surgeon` can now work any shift without new subclasses.
