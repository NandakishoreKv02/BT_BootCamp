---
title: "Clinical Protocol Loader"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 4
difficulty: intermediate
use_case: reference_data
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["file-io", "reading"]
  subtopics: ["readlines", "stripping"]
---

# Lab 4: Clinical Protocol Loader

**Module**: Language Fundamentals  
**Objective**: Read a series of clinical steps from a text file and return them as a clean Python list.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Clinical Guidelines

## Generic Information
**Problem Statement**: Hospital guidelines (e.g., "Sepsis Protocol") are kept in text files. Your app needs to load these steps into a list so they can be displayed one-by-one to a nurse. When reading files, Python includes newline characters (`\n`), which you must remove.

## Use Case
**Title**: Protocol Reader  
**Description**: Load lines from a file into a list.

### Rules
- `load_protocol(filename)`
- Read all lines from the file.
- Strip trailing newlines from each line.
- Return a list of strings.
- Handle `FileNotFoundError` by returning an empty list `[]`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
