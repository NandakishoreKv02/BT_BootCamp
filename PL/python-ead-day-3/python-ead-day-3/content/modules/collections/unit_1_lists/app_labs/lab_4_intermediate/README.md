---
title: "Chronological Sort"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 4
difficulty: intermediate
use_case: appointment_scheduling
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["collections", "lists"]
  subtopics:
    - sorting
    - reverse
    - custom-sort
---

# Lab 4: Chronological Sort

**Module**: Collections
**Objective**: Sort list data to prepare chronological medical reports.
**Difficulty**: Intermediate
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: Appointments are often added in a random order as patients call in. Before printing the daily schedule, the list must be ordered by time.
**Goals**:
- Sort a list of strings (times).
- Use the `.sort()` method.
- Practice reversing a list for "Reverse Chronological" view.

## Use Case
**Title**: Generate Daily Schedule
**Description**: Turn a jumbled list of appointment times into an ordered morning-to-evening schedule.

### Rules
- Sort the list in ascending order.
- Reverse the list for the end-of-day summary.

### Test Cases
- Case 1: Sort `["10:00", "08:00", "09:00"]`, verify result is `["08:00", "09:00", "10:00"]`.
- Case 2: Reverse the sorted list.

### Success Criteria
- Schedule is correctly sequenced.
