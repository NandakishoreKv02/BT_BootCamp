---
title: "Patient Electronic Archive"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 5
difficulty: advanced
use_case: electronic_medical_records
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["io", "dictionaries", "formatting"]
  subtopics: ["data-persistance", "f-strings"]
---

# Lab 5: Patient Electronic Archive

**Module**: Language Fundamentals  
**Objective**: Combine user input collection, dictionary storage, and file writing into a single utility.  
**Difficulty**: Advanced  
**Context**: Healthcare - Medical Records Archiving

## Generic Information
**Problem Statement**: When archiving a patient record, you must gather facts from the clinician and save them to a permanent file. The file should be named using the patient's MRN (Medical Record Number).

## Use Case
**Title**: EMR Archive Tool  
**Description**: Ask for input, create a dictionary, and write to a MRN-named file.

### Rules
- `archive_patient()`
- Ask for: `Patient MRN`, `Full Name`, `Primary Diagnosis`.
- Create a dictionary with these values.
- Open a file named `{MRN}.txt`.
- Write the following 3 lines to the file:
  1. `MRN: {MRN}`
  2. `NAME: {Full Name}`
  3. `DIAGNOSIS: {Primary Diagnosis}`
- Use `with open(...)`.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
