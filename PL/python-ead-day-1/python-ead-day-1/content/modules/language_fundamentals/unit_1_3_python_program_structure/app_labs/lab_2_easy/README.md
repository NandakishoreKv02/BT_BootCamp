---
title: "Vital Signs Validator"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 2
difficulty: easy
use_case: clinical_triage
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["indentation", "logic", "constants"]
  subtopics: ["nested-if", "code-blocks"]
---

# Lab 2: Vital Signs Validator

**Module**: Language Fundamentals  
**Objective**: Implement a triage logic function that relies on correct Python indentation.  
**Difficulty**: Easy  
**Context**: Healthcare - Clinical Triage

## Generic Information
**Problem Statement**: You are building a triage helper for ER nurses. The system needs to categorize a patient's condition based on their Heart Rate (BPM) and Oxygen Saturation (SpO2). The logic involves multiple nested conditions, making correct indentation validation critical.

**Goals**:
- Implement nested logic using indentation
- Define and use constants
- Write clear comments explaining the logic branches

**Data Elements**:
- Heart Rate (int, beats/min)
- SpO2 (int, percentage 0-100)

## Use Case
**Title**: ER Triage Logic  
**Description**: Determine the urgency level ("Critical", "Warning", "Stable") based on vital signs.

### Rules
1. **Critical**: If SpO2 < 90 OR (Heart Rate > 120 AND SpO2 < 95)
2. **Warning**: If SpO2 < 95 OR Heart Rate > 100
3. **Stable**: Everything else

### Test Cases
- Input: HR=80, SpO2=98 -> "Stable"
- Input: HR=110, SpO2=98 -> "Warning" (High HR)
- Input: HR=80, SpO2=94 -> "Warning" (Low SpO2)
- Input: HR=130, SpO2=92 -> "Critical" (High HR + Low SpO2 combination)
- Input: HR=80, SpO2=88 -> "Critical" (Hypoxia)

## Overview
This lab reinforces the importance of using indentation to define logical scope in Python.

## Learning Goals
- Master Python indentation (4 spaces)
- Construct nested `if` statements
- Use constants for magic numbers (e.g., `CRITICAL_SPO2_THRESHOLD = 90`)

## How to Use This Lab
1. Read `tasks.md`
2. Edit `starter_code.py`
3. Run `tests.py` to verify
