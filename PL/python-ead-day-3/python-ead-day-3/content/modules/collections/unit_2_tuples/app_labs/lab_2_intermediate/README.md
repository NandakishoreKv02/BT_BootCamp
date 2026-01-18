---
title: Vital Signs Monitor - Part 2
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 2
difficulty: intermediate
use_case: vital_signs_monitor
domain: healthcare
order: 2
duration_hours: 3
tags:
  topics: ["tuples", "collections"]
  subtopics:
    - unpacking
    - iteration
    - aggregations
---

# Lab 2 (Intermediate): Vital Signs Monitor - Part 2

**Module**: Collections
**Objective**: Analyze tuple data using unpacking and iteration
**Difficulty**: Intermediate
**Context**: Healthcare

## Generic Information
**Problem Statement**: A patient has a list of vital sign readings collected over 24 hours. We need to calculate averages and flag any dangerous readings.
**Goals**:
- Iterate over a list of tuples
- Use tuple unpacking for readable code
- Calculate statistics (Average)
- Filter dangerous values
**Data Elements**: Reading Tuple `(Timestamp, HeartRate, Temp)`

## Use Case
**Title**: Vitals Analyzer
**Description**: A system to process a batch of readings.
**Rules**:
- Readings are immutable tuples: `("08:00", 72, 36.6)`
- High fever is Temp > 38.0
- High heart rate is HR > 100

### Test Cases
- Case 1: Calculate average heart rate correctly
- Case 2: Return list of timestamps where fever was detected
- Case 3: Handle empty list gracefully

### Success Criteria
- Correct use of tuple unpacking `time, hr, temp = reading`
- Accurate math
- Detection logic works

## Overview
Tuples are perfect for "records" that shouldn't change. In this lab, you'll process a series of immutable records. You will practice **unpacking**, which makes Python code incredibly clean when working with tuples.

## Learning Goals
- **Unpacking**: `for time, hr, temp in readings:`
- **Aggregation**: Summing up fields from tuples
- **Filtering**: Selecting tuples based on conditions

## What You'll Build
- `calculate_average_hr(readings)`
- `find_fever_incidents(readings)`
- `generate_summary(readings)`

## Prerequisites
- Completed Lab 1

## Step-by-Step Instructions
1.  Read the tasks.
2.  Implement the logic in `starter_code.py`.
3.  Use the manual test block to verify.
4.  Run `tests.py` for final check.

## Time Estimate
- Implementation: 90 minutes
