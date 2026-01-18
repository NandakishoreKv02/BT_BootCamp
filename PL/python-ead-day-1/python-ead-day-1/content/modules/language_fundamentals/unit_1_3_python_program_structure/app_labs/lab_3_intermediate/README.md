---
title: "Medication Scheduler"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 3
difficulty: intermediate
use_case: medication_timing
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["imports", "datetime", "functions", "main-guard"]
  subtopics: ["datetime-formatting", "constants"]
---

# Lab 3: Medication Scheduler

**Module**: Language Fundamentals  
**Objective**: Build a script that calculates the next medication dose time, demonstrating proper imports and main execution structure.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Patient Management

## Generic Information
**Problem Statement**: Patients usually need to take medication at fixed intervals (e.g., every 4, 6, 8, or 12 hours). You need to write a Python program that takes a "last taken" time and an interval, then calculates the "next dose" time in a human-readable format.

**Goals**:
- Import and use the `datetime` module
- Define specific functions with docstrings
- Use the `__main__` guard logic
- Format time strings

## Use Case
**Title**: Next Dose Calculator  
**Description**: Given a start time (e.g., "08:00") and a frequency in hours, calculate the next dose time.

### Rules
- Support 24-hour time format "HH:MM".
- If the next dose is on the next day, indicate it (e.g., "02:00 (+1 day)").
- Assume the current reference day is today.

### Test Cases
- Last: "08:00", Interval: 4 -> Next: "12:00"
- Last: "20:00", Interval: 6 -> Next: "02:00 (+1 day)"
- Last: "23:00", Interval: 2 -> Next: "01:00 (+1 day)"

## Overview
This lab practices organizing a typical Python script that interacts with standard libraries.

## Learning Goals
- Correctly structure imports (`import datetime`)
- Handle basic time arithmetic
- Modularize logic into functions

## How to Use This Lab
1. Read `tasks.md`
2. Edit `starter_code.py`
3. Run `tests.py`
