---
title: "Vital Sign Monitor"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 3
difficulty: intermediate
use_case: alerts
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["loops", "while-loops"]
  subtopics: ["monitoring", "polling"]
---

# Lab 3: Vital Sign Monitor

**Module**: Language Fundamentals  
**Objective**: Use a `while` loop to simulate continuous polling of a patient's vitals until a stable range is reached or max attempts occur.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Medical Device Interface

## Generic Information
**Problem Statement**: When a blood pressure cuff is inflating, it takes multiple readings until the signal is clear. You need to write a script that "polls" a list of sensor readings using a `while` loop.

## Use Case
**Title**: Signal Stabilization Polling  
**Description**: Continue checking readings until the heart rate is between 60 and 100.

### Rules
- `poll_until_stable(readings)`
- Input: `[150, 120, 110, 85, 75, 70]`
- Logic:
  - Start at the first reading.
  - While reading is NOT in [60, 100], move to the next reading.
  - If you find a reading in range, return it.
  - If you run out of readings without finding one, return `None`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
