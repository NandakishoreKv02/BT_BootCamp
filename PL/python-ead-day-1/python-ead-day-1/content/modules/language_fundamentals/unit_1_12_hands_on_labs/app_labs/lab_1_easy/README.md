---
title: "BMI Calculator & Health Advisor"
type: app_lab
module: language_fundamentals
unit: unit_1_12_hands_on_labs
lab_number: 1
difficulty: easy
use_case: health_assessment
domain: healthcare
order: 1
duration_hours: 2
tags:
  topics: ["integration", "input", "functions", "control-flow"]
  subtopics: ["bmi-calculation", "health-categories"]
---

# Lab 1: BMI Calculator & Health Advisor

**Module**: Language Fundamentals  
**Objective**: Build a complete BMI calculator that collects user input, performs calculations, categorizes results, and provides health recommendations.  
**Difficulty**: Easy  
**Context**: Healthcare - Preventive Medicine

## Generic Information
**Problem Statement**: Create an interactive program that calculates Body Mass Index and provides personalized health advice based on WHO categories.

## Use Case
**Title**: Complete Health Assessment Tool  
**Description**: Integrate input validation, mathematical calculations, conditional logic, and formatted output.

### Requirements
1. Collect height (meters) and weight (kg) from user
2. Validate inputs (positive numbers only)
3. Calculate BMI using formula: weight / (height²)
4. Categorize result:
   - Underweight: < 18.5
   - Normal: 18.5 - 24.9
   - Overweight: 25.0 - 29.9
   - Obese: ≥ 30.0
5. Display formatted report with recommendation

### Functions to Implement
- `get_valid_input(prompt, input_type)`: Collect and validate user input
- `calculate_bmi(weight, height)`: Perform BMI calculation
- `categorize_bmi(bmi)`: Return category string
- `generate_recommendation(category)`: Return health advice
- `display_report(weight, height, bmi, category, recommendation)`: Format output

## How to Use This Lab
1. Read `tasks.md` for detailed implementation steps
2. Edit `starter_code.py`
3. Run `tests.py` to verify correctness
4. Test manually with various inputs

## Expected Output Example
```
=== BMI Health Calculator ===
Enter weight (kg): 70
Enter height (m): 1.75

--- HEALTH ASSESSMENT REPORT ---
Weight: 70.0 kg
Height: 1.75 m
BMI: 22.86
Category: Normal Weight
Recommendation: Maintain your current healthy lifestyle!
```
