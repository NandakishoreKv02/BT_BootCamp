---
title: "Electronic Health Record (EHR) Stub"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 4
difficulty: intermediate
use_case: patient_records
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["dictionaries", "lookups"]
  subtopics: ["mappings", "get-method"]
---

# Lab 4: Electronic Health Record (EHR) Stub

**Module**: Language Fundamentals  
**Objective**: Build a profile manager that stores patient records in a dictionary, mapped by their Medical Record Number (MRN).  
**Difficulty**: Intermediate  
**Context**: Healthcare - Medical Informatics

## Generic Information
**Problem Statement**: Looking up a patient in a list of 10,000 is slow (O(n)). Mapping them by a unique ID in a dictionary is near-instant (O(1)). You need to implement a simple system to add, retrieve, and update patient statuses.

## Use Case
**Title**: MRN Patient Manager  
**Description**: Store and retrieve records by ID.

### Rules
- `add_patient(system, mrn, name, status)` -> Add to the `system` dict.
- `get_patient_status(system, mrn)` -> Return status string. Use `.get()` to return `"Not Found"` if MRN is missing.
- `update_status(system, mrn, new_status)` -> Update the record if it exists.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
