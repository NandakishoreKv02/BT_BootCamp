---
title: "Multi-Vital Alert System"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 3
difficulty: intermediate
use_case: alert_generation
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["logical", "precedence"]
  subtopics: ["safety", "logic"]
---

# Lab 3: Multi-Vital Alert System

**Module**: Language Fundamentals  
**Objective**: Build a robust logical expression that combines multiple vitals (Temp, SpO2, and Consciousness) using `and`, `or`, and `not`.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Patient Monitoring

## Generic Information
**Problem Statement**: One vital sign rarely tells the whole story. A fever might be manageable, unless oxygen is also low. You need to create a function that identifies "High Risk" patients based on specific combinations of data.

## Use Case
**Title**: Critical Care Trigger  
**Description**: Trigger a critical alert if logic conditions are met.

### Rules
Trigger `True` if:
1. (Temperature > 39.0 AND SpO2 < 92)
2. OR (Is_Conscious is False)

Otherwise, return `False`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
