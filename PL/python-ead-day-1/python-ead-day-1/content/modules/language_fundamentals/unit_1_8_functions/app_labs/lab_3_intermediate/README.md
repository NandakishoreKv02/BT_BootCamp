---
title: "Pediatric Multi-Dose Calculator"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 3
difficulty: intermediate
use_case: drug_safety
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["functions", "keyword-arguments"]
  subtopics: ["dosage", "safety"]
---

# Lab 3: Pediatric Multi-Dose Calculator

**Module**: Language Fundamentals  
**Objective**: Build a function with many parameters and practice calling it using keyword arguments to improve safety.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Pediatric Pharmacy

## Generic Information
**Problem Statement**: In pediatrics, a prescription needs:
1.  Base mg/kg.
2.  Patient Weight.
3.  Number of doses per day.
4.  Rounding preference.

When a function has 4+ numbers, it's easy to swap them. Keyword arguments prevent this.

## Use Case
**Title**: Multi-Variable Dosage Logic  
**Description**: Calculate the single dose amount.

### Rules
- `calculate_dosage(mg_per_kg, weight, daily_doses, precision=2)`
- Logic: `(mg_per_kg * weight) / daily_doses`
- Return rounded value.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
