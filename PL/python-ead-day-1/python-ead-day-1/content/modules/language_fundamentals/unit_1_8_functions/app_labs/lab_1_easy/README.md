---
title: "Vital Sign Formatter"
type: app_lab
module: language_fundamentals
unit: unit_1_8_functions
lab_number: 1
difficulty: easy
use_case: reporting
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["functions", "formatting"]
  subtopics: ["strings", "units"]
---

# Lab 1: Vital Sign Formatter

**Module**: Language Fundamentals  
**Objective**: Create a function that standardizes the display of patient vitals with their appropriate units.  
**Difficulty**: Easy  
**Context**: Healthcare - Clinical Documentation

## Generic Information
**Problem Statement**: Nurses enter numbers into the system, but clinical notes must be clear about units (e.g., "72 BPM" vs "72"). You need to write a formatter.

## Use Case
**Title**: Standard Print Utility  
**Description**: Wrap a numeric value and a unit string into a professional label.

### Rules
- `format_vital(name, value, unit)`
- Example: `format_vital("HR", 72, "BPM")` -> `"HR: 72 BPM"`
- Handle the naming with a colon and space.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
