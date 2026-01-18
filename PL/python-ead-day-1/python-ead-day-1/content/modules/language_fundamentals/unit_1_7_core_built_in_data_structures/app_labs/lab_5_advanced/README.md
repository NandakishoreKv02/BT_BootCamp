---
title: "Lab Result Batch Processor"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 5
difficulty: advanced
use_case: clinical_analytics
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["lists", "dictionaries", "nesting"]
  subtopics: ["filtering", "aggregation"]
---

# Lab 5: Lab Result Batch Processor

**Module**: Language Fundamentals  
**Objective**: Practice manipulating a list of dictionaries. You will filter results, aggregate totals, and modify nested fields.  
**Difficulty**: Advanced  
**Context**: Healthcare - Laboratory Information System

## Generic Information
**Problem Statement**: You're building a dashboard for a lab technician. You receive a bulk list of results from various tests. You need to calculate statistics and flag high values.

## Use Case
**Title**: Batch Result Analyzer  
**Description**: Calculate the average value for a specific test type and flag results above a threshold.

### Rules
- `analyze_batch(batch, test_type, threshold)`
- Input: `[{"type": "A", "val": 10}, {"type": "A", "val": 20}]`
- Logic:
  1. Filter for items matching `test_type`.
  2. For those items:
     - Add a key `"is_alert": True` if `val > threshold`, else `False`.
     - Calculate the average `val`.
- Return a tuple: `(average_value, modified_filtered_list)`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
