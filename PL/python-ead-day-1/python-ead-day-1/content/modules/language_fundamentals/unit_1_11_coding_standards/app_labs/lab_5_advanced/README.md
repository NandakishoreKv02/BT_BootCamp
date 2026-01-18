---
title: "The SRP Specialist"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 5
difficulty: advanced
use_case: code_refactoring
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["srp", "refactoring", "maintainability"]
  subtopics: ["helper-functions"]
---

# Lab 5: The SRP Specialist

**Module**: Language Fundamentals  
**Objective**: Refactor a single monolithic function into multiple small, well-named helper functions following the Single Responsibility Principle (SRP).  
**Difficulty**: Advanced  
**Context**: Healthcare - Laboratory Data Pipeline

## Generic Information
**Problem Statement**: You have a function called `process_lab_task` that is 50 lines long. It reads data from a list, calculates averages, checks for abnormal values, and formats a final string. This is a "Code Smell" because one function is doing too much.

## Use Case
**Title**: Modular Pipeline Builder  
**Description**: Break down a monolithic process into 3 specific helpers.

### Rules
- `Helper 1`: `clean_data(raw_list)` -> Returns list of floats.
- `Helper 2`: `analyze_risk(values)` -> Returns `"HIGH"` if any > 140, else `"NORMAL"`.
- `Helper 3`: `format_outcome(risk_status)` -> Returns a decorated string.
- `Orchestrator`: `process_labs(raw_list)` calls all three.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
