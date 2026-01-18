---
title: "Patient Record Formatter"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 1
difficulty: easy
use_case: patient_data_formatting
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["program-structure", "docstrings", "formatting"]
  subtopics: ["basic-structure", "string-formatting", "documentation"]
---

# Lab 1: Patient Record Formatter

**Module**: Language Fundamentals  
**Objective**: Create a simple patient record formatter with proper structure and documentation.  
**Difficulty**: Easy  
**Context**: Healthcare - Patient Data Management

## Generic Information
**Problem Statement**: Healthcare systems need to format patient data consistently for display and reporting. You need to create a module that formats patient records with proper indentation, docstrings, and the `__main__` guard pattern.

**Goals**:
- Write functions with proper docstrings
- Use correct indentation
- Implement the `__main__` guard
- Format patient data as strings

**Data Elements**:
- Patient name (string)
- Patient ID (integer)
- Age (integer)

## Use Case
**Title**: Patient Record Display System  
**Description**: Create a module that formats patient information for display on a hospital dashboard. The module should be importable by other systems while also being runnable for testing.

### Rules
- All functions must have docstrings
- Use 4-space indentation
- Include `__main__` guard for testing
- Format patient ID with leading zeros (PAT-XXXXX)

### Test Cases
- Format patient: name="John Doe", id=42, age=35
- Expected output: "Patient: John Doe (PAT-00042), Age: 35"

### Success Criteria
- All tests pass
- Code has proper structure
- Docstrings are present and correct
- Can be both run and imported

## Overview
This lab introduces you to proper Python program structure through a practical healthcare application.

## Learning Goals
- Practice writing docstrings
- Understand `__main__` guard usage
- Format strings professionally
- Structure code properly

## How to Use This Lab
1. Read `tasks.md` for detailed requirements
2. Complete `starter_code.py`
3. Run `tests.py` to verify your solution
4. Compare with `solution/solution.py` if needed
