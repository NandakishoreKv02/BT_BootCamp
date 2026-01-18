---
title: "BMI Calculator"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 2
difficulty: easy
use_case: clinical_metrics
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["float-math", "operators"]
  subtopics: ["precision", "bmi"]
---

# Lab 2: BMI Calculator

**Module**: Language Fundamentals  
**Objective**: Perform arithmetic operations on floats and manage precision.  
**Difficulty**: Easy  
**Context**: Healthcare - Clinical Metrics

## Generic Information
**Problem Statement**: Calculate Body Mass Index (BMI) from weight (kg) and height (m). The result must be a float rounded to 2 decimal places.

**Data Elements**:
- Weight: Float
- Height: Float
- BMI Formula: `weight / (height * height)`

## Use Case
**Title**: Standard BMI Calc
**Description**: Simple function `calculate_bmi(weight, height)`.

### Rules
- If height is 0 or negative, return `0.0`.
- Result must be rounded to 2 decimals.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
