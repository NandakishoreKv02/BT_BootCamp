---
title: "Encounter Log Append Utility"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 3
difficulty: intermediate
use_case: audit_trails
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["file-io", "append"]
  subtopics: ["open-mode-a", "context-managers"]
---

# Lab 3: Encounter Log Append Utility

**Module**: Language Fundamentals  
**Objective**: Write strings to a persistent text file without overwriting previous data.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Clinical Audit Logging

## Generic Information
**Problem Statement**: When a patient record is accessed, the system must append a timestamp and the user ID to a log file. If you use `'w'` mode, you delete all previous history. You must use `'a'` (append) mode.

## Use Case
**Title**: Activity Logger  
**Description**: Append a single line to a file.

### Rules
- `log_access(filename, user_id, patient_id)`
- Format: `[user_id] accessed [patient_id]`
- Add a newline character `\n` at the end of every line.
- Use `with open(..., 'a')`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
