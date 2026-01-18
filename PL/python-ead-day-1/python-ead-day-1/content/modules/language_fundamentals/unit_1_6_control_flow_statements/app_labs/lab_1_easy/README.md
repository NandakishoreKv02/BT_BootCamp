---
title: "Triage Level Classifier"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 1
difficulty: easy
use_case: alert_generation
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["conditionals", "if-elif-else"]
  subtopics: ["triage", "vitals"]
---

# Lab 1: Triage Level Classifier

**Module**: Language Fundamentals  
**Objective**: Use decision-making logic to categorize patients into standard triage colors.  
**Difficulty**: Easy  
**Context**: Healthcare - Emergency Department

## Generic Information
**Problem Statement**: When a patient enters the ER, their vitals are checked. You need to write a script that assigns a "Triage Color" based on Heart Rate (HR).

**Triage Rules**:
- **RED**: HR > 140 or HR < 40 (Immediate care)
- **YELLOW**: HR > 110 or HR < 50 (Urgent)
- **GREEN**: Everything else (Stable)

## Use Case
**Title**: HR Triage System  
**Description**: Calculate the triage category for an incoming patient record.

### Rules
- `classify_triage(heart_rate)`
- Return the string: "RED", "YELLOW", or "GREEN".

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
