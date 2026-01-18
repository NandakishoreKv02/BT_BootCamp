---
title: "The Great Variable Cleanup"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 1
difficulty: easy
use_case: maintenance
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["pep8", "naming"]
  subtopics: ["snake_case"]
---

# Lab 1: The Great Variable Cleanup

**Module**: Language Fundamentals  
**Objective**: Refactor "legacy" healthcare code that uses poor naming conventions.  
**Difficulty**: Easy  
**Context**: Healthcare - Medical Device Interface

## Generic Information
**Problem Statement**: You've inherited a script from an intern that calculates patient fluid balance. The logic works, but the names are impossible to read (`v1`, `v2`, `flag`). You must refactor it to meet PEP 8 standards.

PEP 8 is the official Python Style Guide — a document that defines how Python code should be written so it is clean, readable, and consistent.
It stands for:
PEP = Python Enhancement Proposal
PEP 8 = Proposal #8 → “Python Style Guide”


## Use Case
**Title**: Clean Fluid Tracker  
**Description**: Rename variables to be descriptive.

### Bad Code Provided
```python
v1 = 1200 # intake
v2 = 800 # output
b = v1 - v2
if b < 0:
    s = "DEFICIT"
else:
    s = "SURPLUS"
```

### Rules
- `refactor_balance_logic(intake_ml, output_ml)`
- Use `snake_case`.
- Names must be descriptive (e.g., `net_balance` instead of `b`).

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
