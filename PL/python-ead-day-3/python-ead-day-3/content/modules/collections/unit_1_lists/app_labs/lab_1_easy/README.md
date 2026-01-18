---
title: "Basic Appointment Log"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 1
difficulty: easy
use_case: appointment_scheduling
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["collections", "lists"]
  subtopics:
    - append
    - len
---

# Lab 1: Basic Appointment Log

**Module**: Collections
**Objective**: Practice basic list creation and addition.
**Difficulty**: Easy
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: The clinic needs a way to log patient names as they arrive.
**Goals**:
- Create an empty list for appointments.
- Add patient names to the list.
- Check how many patients are in line.

## Use Case
**Title**: Arrival Tracking
**Description**: As patients arrive at the desk, their names are appended to the day's arrival list.

### Rules
- Use `.append()` to add names.
- Use `len()` to get the total count.

### Test Cases
- Case 1: Add "John", check count is 1.
- Case 2: Add "Mary", check count is 2.

### Success Criteria
- Names are correctly stored and retrieved in order of arrival.
