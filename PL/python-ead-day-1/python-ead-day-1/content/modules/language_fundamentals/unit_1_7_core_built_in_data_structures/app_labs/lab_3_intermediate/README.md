---
title: "Cross-Patient Allergy Tracker"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 3
difficulty: intermediate
use_case: patient_safety
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["sets", "set-operations"]
  subtopics: ["intersection", "uniqueness"]
---

# Lab 3: Cross-Patient Allergy Tracker

**Module**: Language Fundamentals  
**Objective**: Use sets to find common allergies among groups of patients and to deduplicate allergy lists.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Patient Safety & Epidemiology

## Generic Information
**Problem Statement**: When analyzing patient populations, you often need to find overlapping risks. Sets provide high-performance operations for finding unique items and intersections.

## Use Case
**Title**: Allergy Overlap Analysis  
**Description**: Given two lists of patient allergies (which may contain duplicates), find the unique set of allergies present in BOTH groups.

### Rules
- `get_common_allergies(group_a_list, group_b_list)`
- Input: `["Latex", "Penicillin", "Latex"]`, `["Penicillin", "Peanuts"]`
- Output: `{"Penicillin"}` (as a set)
- Procedure:
  1. Convert both lists to sets (this handles the duplicates within groups).
  2. Use the `intersection()` method or `&` operator.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
