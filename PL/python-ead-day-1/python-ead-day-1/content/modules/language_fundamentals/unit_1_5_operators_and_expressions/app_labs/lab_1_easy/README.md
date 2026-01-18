---
title: "Pediatric Dosage Calculator"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 1
difficulty: easy
use_case: clinical_calculation
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["arithmetic", "division"]
  subtopics: ["dosage", "pediatrics"]
---

# Lab 1: Pediatric Dosage Calculator

**Module**: Language Fundamentals  
**Objective**: Use basic arithmetic operators to calculate weight-based pediatric dosages.  
**Difficulty**: Easy  
**Context**: Healthcare - Clinical Calculator

## Generic Information
**Problem Statement**: In pediatrics, many medications are calculated as "mg per kg". You need to build a function that takes a child's weight and the standard mg/kg dosage, and returns the total amount.

**Formula**:
`Total Dose = Child Weight (kg) * Dosage (mg/kg)`

## Use Case
**Title**: Weight-Based Calculator  
**Description**: Calculate dose for a patient weighing 15.5 kg with a 10mg/kg requirement.

### Rules
- `calculate_mg_dose(weight_kg, mg_per_kg)`
- Return a float rounded to 1 decimal place.
- If weight is <= 0, return 0.0.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
