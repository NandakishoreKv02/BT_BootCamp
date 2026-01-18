---
title: "The Pythonic Patient Portal"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 3
difficulty: intermediate
use_case: membership_management
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["pythonic", "pep8", "classes"]
  subtopics: ["in-operator", "PascalCase"]
---

# Lab 3: The Pythonic Patient Portal

**Module**: Language Fundamentals  
**Objective**: Transition from "C-style" logic to "Pythonic" membership checks and standard class naming.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Patient Admission System

## Generic Information
**Problem Statement**: You have a system that checks if a patient is in a list of "current_admissions". The current developer used a `while` loop with an index and a class named `patient_data`. You need to modernize this code.

## Use Case
**Title**: Admission Search Optimizer  
**Description**: Use PascalCase for classes and the `in` operator for searches.

### Rules
- Rename class `patient_data` to `PatientData`.
- Refactor the search function to use `if name in list:` instead of manual looping.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
