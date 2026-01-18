---
title: "Clinical Data Ingestion Engine"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 6
difficulty: expert
use_case: data_ingestion
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["file-io", "parsing", "reporting"]
  subtopics: ["batch-processing", "f-strings"]
---

# Lab 6: Clinical Data Ingestion Engine

**Module**: Language Fundamentals  
**Objective**: Read a structured log file, parse values, and generate a professional summary report using advanced f-string formatting.  
**Difficulty**: Expert  
**Context**: Healthcare - Laboratory Data Ingestion

## Generic Information
**Problem Statement**: You have a file `daily_vitals.txt` where each line is formatted as `TIMESTAMP|PATIENT_ID|HEART_RATE`. You need to read this file, calculate the average heart rate, and print a formatted summary table.

## Use Case
**Title**: Batch Vitals Summary  
**Description**: Parse values from a pipe-delimited file.

### Input File Format (`daily_vitals.txt`)
```text
0800|P001|72
0815|P002|110
0900|P001|75
```

### Rules
- `generate_vitals_summary(filename)`
- Read all lines.
- Split each line by the pipe `|`.
- Extract the 3rd value (Heart Rate) and convert to `int`.
- Calculate the average (handle empty files/ZeroDivisionError).
- Print a header and each record using f-string padding.
- Print the final Average at the bottom.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
