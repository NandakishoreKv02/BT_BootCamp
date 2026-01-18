---
title: "Hospital Department Manager"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 5
difficulty: advanced
use_case: resource_allocation
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["nested-loops", "indentation", "data-structures"]
  subtopics: ["iterating-dictionaries", "complex-logic"]
---

# Lab 5: Hospital Department Manager

**Module**: Language Fundamentals  
**Objective**: Iterate through deeply nested hospital data structures using correct indentation and logic flow.  
**Difficulty**: Advanced  
**Context**: Healthcare - Resource Management

## Generic Information
**Problem Statement**: You have a nested dictionary representing hospital departments, wards, and bed occupancy. You need to write a report generator that calculates total capacity and occupancy percentages. The logic requires 3-4 levels of nested loops, making indentation errors likely and critical to avoid.

**Goals**:
- Manage deep nesting (3+ levels)
- Write clean, documented helper functions to reduce complexity
- Verify logical scoping with indentation

## Use Case
**Title**: Bed Capacity Report  
**Description**: Traverse a hospital structure to summarize bed usage.

### Data Structure
```python
hospital = {
    "Cardiology": {
        "Ward A": {"occupied": 10, "total": 20},
        "Ward B": {"occupied": 15, "total": 15}
    },
    # ...
}
```

### Rules
- Function `generate_report(hospital_data)` returns a dict: `{"total_beds": X, "total_occupied": Y}`.
- Logic must safely handle empty wards or departments.

## Overview
This lab challenges your ability to keep track of logical scope in complex iterations.

## Learning Goals
- Managing complex code blocks
- Reducing indentation depth (Refactoring technique)

## How to Use This Lab
1. Read `tasks.md`
2. Edit `starter_code.py`
3. Run `tests.py`
