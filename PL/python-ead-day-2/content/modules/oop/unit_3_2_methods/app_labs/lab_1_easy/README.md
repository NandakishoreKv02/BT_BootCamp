---
title: "Clinic Admission Portal"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 1
difficulty: easy
use_case: clinic_workflow
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["oop", "methods"]
  subtopics:
    - instance-methods
    - state-modification
---

# Lab 1: Clinic Admission Portal

**Module**: Object-Oriented Programming - Part 1
**Objective**: Implement basic instance methods to handle patient admission.
**Difficulty**: Easy
**Context**: Clinic Workflow

## Generic Information
**Problem Statement**: The clinic needs a digital way to track whether a patient is currently "admitted" or "discharged".
**Goals**:
- Define a method to admit a patient.
- Define a method to discharge a patient.
- Update instance state based on these actions.
**Data Elements**:
- `name`: Patient Name
- `is_active`: Boolean status

## Use Case
**Title**: Manage Admission Status
**Description**: When a patient arrives, their status should be set to active. When they leave, it should be set to inactive.

### Rules
- A new patient record starts as inactive.
- Methods should return a confirmation string.

### Test Cases
- Case 1: Create patient, verify initial status is False.
- Case 2: Call `admit()`, verify status is True.
- Case 3: Call `discharge()`, verify status is False.

### Success Criteria
- Status is correctly toggled by methods.
- Methods return correct confirmation messages.

## Overview
This is the base lab for clinical workflow automation. We focus purely on how instance methods (using `self`) can change the attributes of a single patient.

---
