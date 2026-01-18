---
title: "Patient Data Parser"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 1
difficulty: easy
use_case: data_entry
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["type-casting", "string-methods"]
  subtopics: ["int", "float", "conversion"]
---

# Lab 1: Patient Data Parser

**Module**: Language Fundamentals  
**Objective**: Convert raw string input from a form into correct Python data types.  
**Difficulty**: Easy  
**Context**: Healthcare - Patient Registration Form

## Generic Information
**Problem Statement**: Web forms and EMR interfaces often send data as strings. You need to parse these strings into `int` (for age, ID) and `float` (for weight, temp) to perform calculations later.

**Goals**:
- Convert string "45" to int 45
- Convert string "70.5" to float 70.5
- Handle basic whitespace issues (trim spaces)

## Use Case
**Title**: Registration Form Processor  
**Description**: Parse fields: ID, Age, Weight, IsSmoker.

### Rules
- `parse_patient_data(id_str, age_str, weight_str, smoker_str)`
- `id_str` -> int
- `age_str` -> int
- `weight_str` -> float
- `smoker_str` -> bool (Assume "Yes"/"True" is True, distinct from "No"/"False")

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py` to implement the parsing logic.
3. Run `tests.py`.
