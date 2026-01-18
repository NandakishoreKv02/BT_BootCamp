---
title: "The Code Cleanup"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 1
difficulty: easy
use_case: refactoring
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["refactoring", "classes", "procedural-to-oop"]
---

# Lab 1: The Code Cleanup

**Module**: Thinking in Objects
**Objective**: Refactor a messy procedural script that tracks patient waiting times into a clean `WaitingRoom` class.
**Difficulty**: Easy
**Context**: Outpatient Clinic

## Problem Statement
The starter code uses two global lists `names` and `times`. It has functions that operate on these globals. This is hard to maintain. You must encapsulate this logic into a class.

## Requirements
1.  **Class**: `WaitingRoom`.
2.  **Attributes**: `queue` (a dictionary or list of tuples).
3.  **Methods**:
    - `check_in(name, time)`
    - `get_wait_time(name)`: Returns the time or -1 if not found.
4.  **Goal**: Eliminate all global variables.

## Expected Output
```text
Checked in Alice at 10:00.
Checked in Bob at 10:15.
Alice entered at 10:00.
```
