---
title: "Clinical Thresholds"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 3
difficulty: intermediate
use_case: alert_system
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["constants", "boolean-logic"]
  subtopics: ["magic-numbers", "naming-conventions"]
---

# Lab 3: Clinical Thresholds

**Module**: Language Fundamentals  
**Objective**: Replace "magic numbers" with properly named constants and implement Boolean check functions.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Alert System

## Generic Information
**Problem Statement**: Hardcoded numbers like `100.4` or `90` are bad practice. They convey no meaning. You often need to define standardized thresholds (constants) and use them to return Boolean statuses (e.g., `is_fever(temp)`).

**Goals**:
- Define PEP 8 compliant constants (e.g., `FEVER_THRESHOLD`).
- Write functions that return `bool`.

## Use Case
**Title**: Vitals Value Checker
**Description**: Check Temperature and Blood Pressure.

### Rules
- `is_fever(temp_celsius)`: Returns True if >= `38.0`.
- `is_called_hypertensive(systolic, diastolic)`: Returns True if systolic >= `140` OR diastolic >= `90`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
