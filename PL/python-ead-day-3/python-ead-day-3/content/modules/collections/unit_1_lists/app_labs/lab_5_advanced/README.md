---
title: "Patient Queue Audit"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 5
difficulty: advanced
use_case: appointment_scheduling
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["collections", "lists"]
  subtopics:
    - indexing
    - counting
    - membership
---

# Lab 5: Patient Queue Audit

**Module**: Collections
**Objective**: Perform deep inspection of list data to identify patterns and specific records.
**Difficulty**: Advanced
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: The clinic manager wants to know if certain patients are "frequent flyers" (appearing multiple times in the queue) and exactly where an emergency patient is located in the line.
**Goals**:
- Use `.count()` to find duplicates.
- Use `.index()` to find exact positions.
- Handle search errors gracefully.

## Use Case
**Title**: Search and Audit
**Description**: Find how many appointments "Alice" has today and verify the position of the first "Emergency" tag.

### Rules
- If "Emergency" doesn't exist, handle the `ValueError` (or check with `in`).
- Use `.count()` for frequency analysis.

### Test Cases
- Case 1: Search for a name that appears twice, verify count is 2.
- Case 2: Find index of a name, verify correctness.

### Success Criteria
- Accurate location and frequency data reported for the audit.
