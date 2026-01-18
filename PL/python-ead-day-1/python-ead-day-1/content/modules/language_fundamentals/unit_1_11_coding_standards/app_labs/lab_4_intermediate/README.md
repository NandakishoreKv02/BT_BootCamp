---
title: "The Clean Documentation Cure"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 4
difficulty: intermediate
use_case: knowledge_transfer
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["docstrings", "pep8", "formatting"]
  subtopics: ["google-style-docstrings"]
---

# Lab 4: The Clean Documentation Cure

**Module**: Language Fundamentals  
**Objective**: Apply professional docstrings and PEP 8 formatting to a complex dosage calculation function.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Pharmacokinetic Modeling

## Generic Information
**Problem Statement**: You have a function that calculates drug concentration over time. The math is correct, but there are no comments, the params are single letters (`d`, `t`, `h`), and the spacing is non-existent. You must refactor it for high readability.

## Use Case
**Title**: Readable Dosage Engine  
**Description**: Rename parameters and add comprehensive Docstrings.

### Rules
- Rename parameters to `dose_mg`, `time_hours`, and `half_life`.
- Add a triple-quoted Docstring explaining "Args", "Returns", and "Raises" (even if it doesn't raise anything yet).
- Fix spacing around operators (e.g., `x+y` -> `x + y`).

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
