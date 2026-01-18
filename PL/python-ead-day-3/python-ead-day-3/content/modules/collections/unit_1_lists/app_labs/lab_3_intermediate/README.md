---
title: "Doctor-Specific Filtering"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 3
difficulty: intermediate
use_case: appointment_scheduling
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["collections", "lists"]
  subtopics:
    - list-comprehensions
    - filtering
---

# Lab 3: Doctor-Specific Filtering

**Module**: Collections
**Objective**: Use list comprehensions to extract specific data from a master schedule.
**Difficulty**: Intermediate
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: A central database stores all appointments for the clinic. However, Dr. Smith only needs to see their own patients.
**Goals**:
- Filter a list of dictionaries based on a specific key value.
- Use list comprehension for concise implementation.

## Use Case
**Title**: View My Patients
**Description**: Dr. Smith logs in. The system must filter the `master_schedule` and return only appointments where the `doctor` is "Smith".

### Rules
- Use a list comprehension to create the new list.
- Data format: `{"patient": "Name", "doctor": "Name"}`.

### Test Cases
- Case 1: Filter 10 appointments, verify only "Smith" entries remain.
- Case 2: Filter with a name that doesn't exist, verify return is an empty list.

### Success Criteria
- The output list contains only the relevant patient objects.
