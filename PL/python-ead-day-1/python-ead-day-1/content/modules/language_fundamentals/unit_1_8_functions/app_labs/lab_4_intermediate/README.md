---
title: "Encapsulated Triage logic"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 4
difficulty: intermediate
use_case: patient_prioritization
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["functions", "scope"]
  subtopics: ["local-variables", "guard-clauses"]
---

# Lab 4: Encapsulated Triage Logic

**Module**: Language Fundamentals  
**Objective**: Practice variable scope and early returns (guard clauses) in a decision-making function.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Emergency Triage

## Generic Information
**Problem Statement**: When a vital exceeds a critical limit, we need to return immediately with a "CRITICAL" flag. Otherwise, check lower levels. This lab tests your ability to manage logic inside functions and keep variables local.

## Use Case
**Title**: Systolic BP Triage  
**Description**: Return category based on systolic BP.

### Rules
- `get_triage_category(systolic_bp)`
- BP > 180: "CRITICAL"
- BP > 140: "URGENT"
- BP > 120: "ELEVATED"
- Otherwise: "NORMAL"
- Use multiple `if` statements with `return` to avoid deep nesting.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
