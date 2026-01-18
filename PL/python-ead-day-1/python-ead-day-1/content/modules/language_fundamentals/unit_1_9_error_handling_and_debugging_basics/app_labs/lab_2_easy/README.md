---
title: "Lab Result History Navigator"
type: app_lab
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
lab_number: 2
difficulty: easy
use_case: data_retrieval
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["error-handling", "lists"]
  subtopics: ["indexerror"]
---

# Lab 2: Lab Result History Navigator

**Module**: Language Fundamentals  
**Objective**: Handle `IndexError` when attempting to access specific historical results from a clinical list.  
**Difficulty**: Easy  
**Context**: Healthcare - Laboratory Information System (LIS)

## Generic Information
**Problem Statement**: Doctors often ask for the "most recent" or "2nd most recent" result. If a patient only has one result, asking for the 2nd one will crash the program. You must handle this elegantly.

## Use Case
**Title**: Historical Data Accessor  
**Description**: Retrieve an item at a specific index.

### Rules
- `get_historical_result(results_list, offset)`
- Input: `[10, 20, 30], 1` -> Should return `20` (index 1).
- Input: `[10], 5` -> Out of bounds. Handle `IndexError`.
- Output for error: Return `"Result Not Available"`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
