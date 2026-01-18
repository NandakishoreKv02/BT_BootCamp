---
title: "Clinic-Wide Census tracking"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 3
difficulty: intermediate
use_case: hospital_administration
domain: healthcare
order: 3
duration_hours: 2
tags:
  topics: ["oop", "class-methods"]
  subtopics:
    - class-variables
    - class-methods
    - state-management
---

# Lab 3: Clinic-Wide Census tracking

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master shared state management using class variables and class methods.
**Difficulty**: Intermediate
**Context**: Hospital Administration

## Generic Information
**Problem Statement**: Individual patient data is useful, but the clinic manager needs to know how many patients are in the facility at any given moment without looping through every object.
**Goals**:
- Use a class variable to track the total number of admitted patients.
- Use a class method to retrieve this global count.
**Data Elements**:
- `total_admitted`: Class-level integer.

## Use Case
**Title**: Track Facility Occupancy
**Description**: When a patient is admitted (Lab 1 logic), the global census increases. When discharged, it decreases.

### Rules
- Global count cannot be less than zero.
- Only the `Patient` class should manage this count.

### Test Cases
- Case 1: Admit two patients, census should be 2.
- Case 2: Discharge one, census should be 1.

### Success Criteria
- Census is updated automatically by instance methods but accessible via a class method.

## Overview
This lab introduces the `@classmethod` decorator and the `cls` parameter, showing how to interact with data that belongs to the group rather than the individual.

---
