---
title: "IV Flow Rate Calculator"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 2
difficulty: easy
use_case: patient_care
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["functions", "parameters"]
  subtopics: ["defaults", "math"]
---

# Lab 2: IV Flow Rate Calculator

**Module**: Language Fundamentals  
**Objective**: Use default parameters to create a flexible calculation utility.  
**Difficulty**: Easy  
**Context**: Healthcare - Infusion Nursing

## Generic Information
**Problem Statement**: Calculating IV flow rate (mL/hr) is simple: `Total Volume / Total Time`. Often, the time is standard (1 hour). You want a function that defaults to 1 hour but can be overridden.

## Use Case
**Title**: Infusion Speed Logic  
**Description**: Divide volume by hours.

### Rules
- `calculate_flow_rate(volume_ml, time_hr=1.0)`
- Input: `500, 2` -> Output: `250.0`
- Input: `100` -> Output: `100.0` (using default)
- Return value should be a float.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
