---
title: "Dynamic Formula Evaluator"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 6
difficulty: expert
use_case: patient_metrics
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["precedence", "dynamic-eval"]
  subtopics: ["formulas", "risk-scores"]
---

# Lab 6: Dynamic Formula Evaluator

**Module**: Language Fundamentals  
**Objective**: Build a utility that calculates complex medical risk scores by interpreting a series of input variables. This lab tests your understanding of multi-variable logic and mathematical precedence.  
**Difficulty**: Expert  
**Context**: Healthcare - Clinical Decision Support (CDS)

## Generic Information
**Problem Statement**: Clinical scores like the "CHADS2" or "HASBLED" use multiple inputs to determine risk. You need to write a generalized evaluator that calculates a simplified "Cardiac Risk Score" (CRS) based on 3 factors:
1.  **Age Adjustment**: `(Age / 10)` - Floor Division.
2.  **Vital Factor**: `(Blood Pressure Systolic - 120) * 0.5`.
3.  **Lab Factor**: `2.0` if `Diabetes is True`, otherwise `0.0`.

**Formula**:
`CRS = Age_Adj + Vital_Factor + Lab_Factor`

## Use Case
**Title**: Simplified Cardiac Risk Score  
**Description**: Input patient data and return a risk score.

### Rules
- `calculate_risk_score(age, sys_bp, has_diabetes)`
- Use `//` for age adjustment.
- Use precedence for vital factor calculation.
- Final result should be rounded to 1 decimal.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
