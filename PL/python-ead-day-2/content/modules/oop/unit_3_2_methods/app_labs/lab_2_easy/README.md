---
title: "Real-time Vitals Update"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 2
difficulty: easy
use_case: patient_monitoring
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["oop", "methods"]
  subtopics:
    - instance-methods
    - validation
---

# Lab 2: Real-time Vitals Update

**Module**: Object-Oriented Programming - Part 1
**Objective**: Implement instance methods with basic parameter validation.
**Difficulty**: Easy
**Context**: Patient Monitoring

## Generic Information
**Problem Statement**: Manual vitals entry is prone to typos. The system needs methods to update temperature and heart rate with basic safety checks.
**Goals**:
- Store temperature and heart rate.
- Implement methods to update these values.
- Ensure values are within a physically possible range.

## Use Case
**Title**: Update Vitals
**Description**: A nurse updates a patient's temperature. The system should only accept the update if the value is between 30°C and 45°C.

### Rules
- Temperature must be between 30.0 and 45.0.
- Heart rate must be between 0 and 300.

### Test Cases
- Case 1: Valid temp update (37.0) succeeds.
- Case 2: Invalid temp update (99.0) is ignored.

### Success Criteria
- Attributes only change if validation passes.

## Overview
Building on Lab 1, we add parameters to our instance methods and use them to safely modify the object's state.

---
