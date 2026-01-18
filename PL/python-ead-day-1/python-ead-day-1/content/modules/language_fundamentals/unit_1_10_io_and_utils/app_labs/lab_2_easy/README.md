---
title: "Clinical Shift Report Generator"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 2
difficulty: easy
use_case: reporting
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["f-strings", "formatting"]
  subtopics: ["padding", "alignment"]
---

# Lab 2: Clinical Shift Report Generator

**Module**: Language Fundamentals  
**Objective**: Use f-strings to create a perfectly aligned clinical summary report.  
**Difficulty**: Easy  
**Context**: Healthcare - Nursing Shift Coordination

## Generic Information
**Problem Statement**: When a nurse finishes a shift, they generate a summary table. If the data isn't aligned, it's difficult for the next shift to read quickly. You must use f-string padding to ensure columns are standard widths.

## Use Case
**Title**: Pro Report Formatter  
**Description**: Return a formatted string for a patient row.

### Rules
- `generate_report_row(patient_id, vitals_count, status)`
- `patient_id`: Left-aligned, 10 spaces.
- `vitals_count`: Right-aligned, 5 spaces.
- `status`: Right-aligned, 12 spaces.
- Separator: Pipe symbol `|`.
- Example Output: `"SID-450    |   12 |   STABILIZED"`

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
