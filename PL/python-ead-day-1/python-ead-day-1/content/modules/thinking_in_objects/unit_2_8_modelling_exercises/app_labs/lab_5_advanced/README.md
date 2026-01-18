---
title: "Multi-Clinic Specialty Network"
type: app_lab
module: thinking_in_objects
unit: unit_2_8_modelling_exercises
lab_number: 5
difficulty: advanced
use_case: complex-multiplicity-modelling
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["many-to-many", "aggregation", "ecosystem"]
---

# Lab 5: Multi-Clinic Specialty Network

**Module**: Thinking in Objects
**Objective**: Architecture a complex, shared network including Many-to-Many relationships and bidirectional sync.
**Difficulty**: Advanced
**Context**: Regional Health Authority

## Problem Statement
A medical specialty network consists of multiple `Clinic` objects and multiple `Specialist` doctors.
1.  **M:N Aggregation**: A `Clinic` features many `Specialist` doctors. A `Specialist` works at many `Clinic` locations.
2.  **State Sync**: When a doctor is added to a clinic, the clinic must be added to the doctor's "Active Locations" list.

## Requirements
1.  **Architecture**:
    - `Clinic` (name, list of specialists).
    - `Specialist` (name, list of clinics).
2.  **Implementation**:
    - Build a method `onboard_specialist(self, specialist_obj)` in the `Clinic` class.
    - This method must update BOTH the clinic's staff list and the specialist's location list.

## Expected Output
```text
Onboarding Dr. House to Princeton Clinic...
Princeton Specialists: ['Dr. House']
Dr. House's Active Clinics: ['Princeton Clinic']
```
