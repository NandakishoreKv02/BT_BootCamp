---
title: "Morning vs Afternoon Slots"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 6
difficulty: advanced
use_case: appointment_scheduling
domain: healthcare
order: 6
duration_hours: 2.5
tags:
  topics: ["collections", "lists"]
  subtopics:
    - slicing
    - list-copying
---

# Lab 6: Morning vs Afternoon Slots

**Module**: Collections
**Objective**: Use list slicing to create sub-groups of data for reporting.
**Difficulty**: Advanced
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: The clinic operates in two shifts. We need to split the master list of 24 hourly slots into a "Morning Shift" and an "Afternoon Shift" for the respective staff.
**Goals**:
- Use slicing syntax `[start:stop:step]`.
- Create new lists from segments of an existing list.
- Extract every 2nd slot for a "Quick Checkup" report.

## Use Case
**Title**: Shift Reporting
**Description**: Split the list at the 12th index (mid-day). Extract a special report for every other patient to balance the nurse's load.

### Rules
- Morning: Indexes 0 to 11.
- Afternoon: Indexes 12 to 23.
- Quick Report: Every 2nd patient from the whole list.

### Test Cases
- Case 1: Slice the first 12, verify length.
- Case 2: Slice from 12 onwards, verify length.
- Case 3: Slice with step 2.

### Success Criteria
- Sub-lists are created accurately without modifying the original master list.
