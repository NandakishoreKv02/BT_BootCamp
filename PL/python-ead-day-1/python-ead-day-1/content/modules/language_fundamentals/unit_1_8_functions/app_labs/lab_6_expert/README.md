---
title: "Clinical Risk Score Orchestrator"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 6
difficulty: expert
use_case: clinical_decision_support
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["functions", "modularization"]
  subtopics: ["helper-functions", "abstraction"]
---

# Lab 6: Clinical Risk Score Orchestrator

**Module**: Language Fundamentals  
**Objective**: Practice the "Single Responsibility Principle" by building a main orchestrator function that delegates specific calculations to helper functions.  
**Difficulty**: Expert  
**Context**: Healthcare - Advanced Risk Analysis

## Generic Information
**Problem Statement**: Medical risk scores are often composed of multiple sub-scores (Cardiology + Pulmonary + Lab). Instead of one giant function, you should have one function that calls three small ones. This makes the code easier to test and update.

## Use Case
**Title**: Modular Risk Engine  
**Description**: Calculate a total risk percentage.

### Sub-Calculations
1.  **Age Risk**: 1% risk for every 10 years of age.
2.  **Vital Risk**: 5% if HR > 100, else 0%.
3.  **Lab Risk**: 10% if Diabetes is True, else 0%.

### Rules
- `get_total_risk(age, hr, has_diabetes)`
- Inside, it MUST call:
  - `_calc_age_factor(age)`
  - `_calc_vital_factor(hr)`
  - `_calc_lab_factor(has_diabetes)`
- Return the sum of all factors.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
