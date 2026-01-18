---
title: "Patient Profile Generator"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 5
difficulty: advanced
use_case: electronic_health_records
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["functions", "docstrings"]
  subtopics: ["dictionary-returns", "documentation"]
---

# Lab 5: Patient Profile Generator

**Module**: Language Fundamentals  
**Objective**: Practice documenting functions with Docstrings and returning complex data structures (dictionaries).  
**Difficulty**: Advanced  
**Context**: Healthcare - EHR System Integration

## Generic Information
**Problem Statement**: When creating a record in a database, you often use a function to "clean and package" raw inputs into a dictionary. This function needs clear documentation so other developers know what data is expected.

## Use Case
**Title**: Record Packager  
**Description**: Transform individual inputs into a structured patient dictionary.

### Rules
- `create_patient_record(first_name, last_name, age, city="Unknown")`
- Return key-value pairs: `{"full_name": "LAST, FIRST", "age_years": age, "location": city}`.
- Include a Google-style or PEP 257 Docstring.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
