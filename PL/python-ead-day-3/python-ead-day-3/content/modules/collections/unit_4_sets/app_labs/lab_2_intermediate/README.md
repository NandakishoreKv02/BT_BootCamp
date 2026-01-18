---
title: "Cross-Department Patient Analysis"
type: app_lab
module: collections
unit: unit_4_sets
lab_number: 2
difficulty: intermediate
use_case: patient_flow_analysis
domain: healthcare
order: 2
duration_hours: 3
tags:
  topics: ["sets", "collections"]
  subtopics:
    - intersection
    - union
    - difference
    - symmetric-difference
---

# Lab 2 (Intermediate): Cross-Department Patient Analysis

## Generic Information
**Problem Statement**: Hospital administrators need to understand how patients flow between departments. Specifically, identifying patients who appear in multiple registries (e.g., ER and ICU) or those who are only in one.

**Goals**:
- Identify patients visiting both ER and ICU.
- Find the total pool of unique patients across multiple departments.
- Isolate patients who visited the ER but were not admitted to the ICU.

**Data Elements**:
- `er_patients`: Set of patient IDs from the Emergency Room.
- `icu_patients`: Set of patient IDs from the Intensive Care Unit.

## Use Case
**Title**: Analyze Patient Flow
**Description**: Use set mathematics to compare department registries and generate insights on patient admissions and overlaps.

### Rules
- Use symbolic operators (`&`, `|`, `-`, `^`) for set comparisons.
- Handle empty sets without errors.
- Ensure results are returned as sets.

### Test Cases
- Case 1: Intersection correctly finds patients in both sets.
- Case 2: Union correctly combines all unique patients.
- Case 3: Difference correctly finds patients in the primary set only.

### Success Criteria
- [ ] Intersections accurately identify overlaps.
- [ ] Unions provide a complete deduplicated list.
- [ ] Differences correctly isolate unique department visitors.

## Overview
This lab moves beyond basic modification into set theory. You will implement logic that answers complex questions about cross-department data using concise set operators.

## How to Use This Lab
1. Implement the analysis functions in `starter_code.py`.
2. Use set operators for maximum readability and performance.
3. Test with `tests.py`.
