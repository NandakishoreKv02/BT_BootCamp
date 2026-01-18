---
title: Vital Signs Monitor - Part 3
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 3
difficulty: advanced
use_case: vital_signs_monitor
domain: healthcare
order: 3
duration_hours: 4
tags:
  topics: ["tuples", "collections"]
  subtopics:
    - namedtuple
    - time-series
    - complex-returns
    - zipping
---

# Lab 3 (Advanced): Vital Signs Monitor - Part 3

**Module**: Collections
**Objective**: specific focus on advanced tuple structures and time-series analysis
**Difficulty**: Advanced
**Context**: Healthcare

## Generic Information
**Problem Statement**: Doctors need to know how vitals represent *change* over time, not just static values. We need to calculate rate of change and structured reports.
**Goals**:
- Use `namedtuple` for clearer data representation
- Calculate deltas between consecutive readings
- Return complex multi-value results
**Data Elements**: Readings, Alerts

## Use Case
**Title**: Vital Trends Analyzer
**Description**: A system to track the *trajectory* of patient health.
**Rules**:
- Significant change: HR change > 20 bpm between readings.
- Use `namedtuple` "Reading" with fields `time`, `hr`, `temp`.

### Test Cases
- Case 1: Detect rapid HR spike
- Case 2: Convert list of tuples to list of namedtuples
- Case 3: Calculate deltas correctly zipping list with itself offset by 1

### Success Criteria
- Code uses `collections.namedtuple`
- Logic correctly identifies changes between row N and N+1

## Overview
Tuples are great, but `reading[1]` is hard to read. In this advanced lab, you'll upgrade to **namedtuples**, which are like lightweight objects. You will also perform "window functions"—looking at the previous value to see how much things changed.

## Learning Goals
- **namedtuple**: Creating self-documenting tuples
- **Time-Series Logic**: Comparing `i` and `i-1`
- **zip()**: Iterating pairs `(current, next)`

## What You'll Build
- `convert_to_namedtuples(readings)`
- `analyze_trends(readings)`
- `find_rapid_changes(readings)`

## Prerequisites
- Completed Lab 2

## Time Estimate
- Implementation: 120 minutes

## Key Concepts Practiced
- `from collections import namedtuple`
- `zip(data[:-1], data[1:])` idiom for pairs
