---
title: Hospital Analytics System
type: app_lab
module: collections
unit: unit_3_dictionaries
lab_number: 3
difficulty: advanced
use_case: hospital_analytics
domain: healthcare
order: 3
duration_hours: 4
tags:
  topics: ["dictionaries", "collections"]
  subtopics:
    - merging
    - filtering-advanced
    - aggregation
    - validation
    - comprehensions
---

# Lab 3 (Advanced): Hospital Analytics System

**Module**: Collections
**Objective**: Build a robust data processing system for hospital records.
**Difficulty**: Advanced
**Context**: Healthcare

## Generic Information
**Problem Statement**: The hospital needs to merge patient records from an old archive system, clean up inconsistent data, and generate demographic reports for the board of directors.
**Goals**:
- Merge two large datasets while handling conflicts
- Clean and validate data against a strict schema
- Perform complex multi-criteria searches
- Aggregate statistics efficiently
**Data Elements**: Patient Records (ID, Name, Age, Blood Type, Status, Last Visit)

## Use Case
**Title**: Data Warehouse & Analytics Engine
**Description**: A system to ingest, clean, and analyze patient data from multiple sources.
**Rules**:
- **Merging**: If a patient exists in both `current` and `archive`, keep the `current` version but log the conflict.
- **Validation**: Every record MUST have `name` and `age`. If missing, mark as "Incomplete".
- **Analytics**: Reports must be generated using efficient dictionary comprehensions.

### Test Cases
- Case 1: Merge archive dictionary into main database with overlap
- Case 2: Validate a dataset containing corrupt records
- Case 3: Search for patients "Age > 50 AND Blood Type = O+"
- Case 4: Group patients by Blood Type (Aggregation)

### Success Criteria
- Merging logic preserves data integrity
- Validation function correctly identifies all bad records
- Search engine handles arbitrary criteria
- Code uses dictionary comprehensions for performance

## Overview
This is an **Advanced** lab. You are moving from managing individual records (Lab 1) and hierarchies (Lab 2) to **processing entire datasets**.

You will deal with "dirty data", merge conflicts, and the need for speed. This mirrors real-world backend engineering where data isn't always perfect, and business logic gets messy.

## Learning Goals
- **Merge Dictionaries**: Using `.update( )` vs manual merging logic
- **Data Validation**: Checking keys and types dynamically
- **Advanced Comprehensions**: Creating dictionaries from filtered data
- **Grouping/Aggregation**: Transforming `{id: data}` into `{category: [ids]}`

## The Scenario
The IT department is migrating an old legacy system ("Archive DB") into the modern platform ("Main DB").
1.  **Merge**: You need to combine them. Warning: Some IDs might clash.
2.  **Clean**: The old system didn't enforce rules, so some records are missing names or ages. You need to tag them.
3.  **Analyze**: The Director wants a breakdown of patients by blood type and a list of all seniors (65+).

## What You'll Build
- `merge_datasets(main, archive)`: Smart merging logic.
- `validate_schema(db)`: Data cleaner.
- `advanced_search(db, criteria)`: A flexible query engine.
- `generate_demographics(db)`: A grouping engine.

## Prerequisites
- Completed Lab 2 (Intermediate)
- Strong grasp of loops and conditionals
- Understanding of dictionary complexity O(1)

## How to Use This Lab
1. **Read** `README.md`
2. **Study** `tasks.md` (pay attention to edge cases)
3. **Start** with `starter_code.py`
4. **Implement** robustly—think "Production Code"
5. **Run** `tests.py`

## Task Summary
- Task 1: Safe Merge with Conflict Logging
- Task 2: Schema Validation & Cleaning
- Task 3: Advanced Multi-Criteria Search
- Task 4: Demographic Aggregation

## Time Estimate
- Reading & Design: 30 minutes
- Implementation: 2-3 hours
- Testing: 1 hour
- **Total**: 3.5-4.5 hours

## Key Concepts Practiced
- Dictionary `.update()` vs manual loops
- `try-except` blocks for data cleaning
- List/Dict Comprehensions for filtering
- `collections.defaultdict` (optional but recommended for grouping)

## Common Pitfalls
- **Shallow Copies**: Modifying a merged dict might affect the original if not careful (though for this lab, modifying in-place is acceptable if documented).
- **Inefficient Search**: loop-inside-loop is O(N*M). Try to keep it O(N).

## Next Steps
After Lab 3:
1. You have mastered Python Dictionaries!
2. You can handle complex data pipelines.
3. Next Module: Sets (Unit 4) will help with uniqueness problems even more.
