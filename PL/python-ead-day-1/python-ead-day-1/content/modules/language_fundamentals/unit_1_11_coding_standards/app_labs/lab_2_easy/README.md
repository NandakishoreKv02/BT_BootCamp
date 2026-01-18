---
title: "The Magic Number Mirror"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 2
difficulty: easy
use_case: patient_safety
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["pep8", "constants"]
  subtopics: ["SCREAMING_SNAKE_CASE"]
---

# Lab 2: The Magic Number Mirror

**Module**: Language Fundamentals  
**Objective**: Identify and eliminate "magic numbers" by using named constants.  
**Difficulty**: Easy  
**Context**: Healthcare - Vital Signs Thresholds

## Generic Information
**Problem Statement**: You are building an alerting system for heart rates. The "normal" range (60 to 100) is hardcoded inside the function. If clinical guidelines change, you have to search through code to find every `100`. You must move these to the top of the file as constants.

## Use Case
**Title**: Alert Threshold Manager  
**Description**: Define and use constants for range checks.

### Rules
- Define `MIN_NORMAL_HR` (60) and `MAX_NORMAL_HR` (100).
- Create a function `check_vital_alert(heart_rate)`.
- If heart rate is outside the range, return `"ALERT"`.
- Else, return `"NORMAL"`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
