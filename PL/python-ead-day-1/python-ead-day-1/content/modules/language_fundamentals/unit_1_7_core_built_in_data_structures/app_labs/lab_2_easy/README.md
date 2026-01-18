---
title: "Clinical Reference Ranges"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 2
difficulty: easy
use_case: reference_lookups
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["tuples", "immutability"]
  subtopics: ["lookup", "unpacking"]
---

# Lab 2: Clinical Reference Ranges

**Module**: Language Fundamentals  
**Objective**: Use tuples to store and unpack clinical reference ranges (Normal Min, Normal Max).  
**Difficulty**: Easy  
**Context**: Healthcare - Clinical Decision Support

## Generic Information
**Problem Statement**: Reference ranges (e.g., normal HR is 60-100) are static facts. You should store them in a way that prevents accidental changes. Tuples are perfect for this.

## Use Case
**Title**: HR Reference Unpacker  
**Description**: Retrieve the min and max for a reading and check if a given value is in range.

### Rules
- `get_hr_range()` -> returns tuple `(60, 100)`.
- `is_value_normal(value, reference_tuple)` -> Unpack tuple, compare value, return `True/False`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
