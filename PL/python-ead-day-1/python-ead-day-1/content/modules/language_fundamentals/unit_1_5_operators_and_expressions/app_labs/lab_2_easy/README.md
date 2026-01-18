---
title: "Triage Alert Logic"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 2
difficulty: easy
use_case: alert_generation
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["comparison", "logic"]
  subtopics: ["triage", "vitals"]
---

# Lab 2: Triage Alert Logic

**Module**: Language Fundamentals  
**Objective**: Use basic comparison operators to identify patients in "Red" (Emergency) or "Observation" status based on heart rate.  
**Difficulty**: Easy  
**Context**: Healthcare - Emergency Department

## Generic Information
**Problem Statement**: In a busy ER, computers monitor patient vitals. You need to write a logical check that returns `True` if a heart rate is outside the safe range (60 to 100).

## Use Case
**Title**: HR Range Alert  
**Description**: Check if heart rate is dangerously low (< 60) or high (> 100).

### Rules
- `is_alert_triggered(heart_rate)`
- Return `True` if HR is < 60 OR HR is > 100.
- Otherwise return `False`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
