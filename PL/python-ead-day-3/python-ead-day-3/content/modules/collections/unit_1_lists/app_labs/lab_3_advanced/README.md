---
title: Appointment Scheduling - Part 3
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 3
difficulty: advanced
use_case: appointment_scheduling
domain: healthcare
order: 3
duration_hours: 4
tags:
  topics: ["lists", "collections"]
  subtopics:
    - inserting
    - extending
    - comprehensions
    - optimization
---

# Lab 3 (Advanced): Appointment Scheduling - Part 3

**Module**: Collections
**Objective**: specific focus on advanced list operations and performance
**Difficulty**: Advanced
**Context**: Healthcare

## Generic Information
**Problem Statement**: The clinic needs to manage a waitlist, insert VIP/Emergency cases into the active queue, and analyze slot efficiency.
**Goals**:
- Batch process the waitlist
- Handle emergency insertions (Priority Queue logic)
- Analyze data using list comprehensions
**Data Elements**: Schedule Lists, Waitlist Lists

## Use Case
**Title**: Advanced Waitlist Manager
**Description**: A system to move people from waitlist to active schedule, handle emergency squeeze-ins, and format reports efficiently.
**Rules**:
- Waitlist is processed in batches (FIFO).
- Emergencies must be inserted at index 0 or specific index.
- Duplicate names should be prevented.

### Test Cases
- Case 1: Batch move waitlist to schedule
- Case 2: Insert emergency at start
- Case 3: Filter duplicates using comprehension
- Case 4: Format report with index numbers

### Success Criteria
- Waitlist clears correctly
- Schedule order is maintained correctly
- Comprehensions are used for concise code

## Overview
In the final part of this series, you'll tackle **bulk operations** and **insertions**. Unlike `.append()` which is O(1), `.insert()` is O(N). You'll learn when to use which. You'll also use **List Comprehensions**, a powerful Python feature to transform lists in one line.

## Learning Goals
- **Batch Add**: Using `.extend()`
- **Insert**: Using `.insert()` vs Slicing
- **Comprehensions**: `[x for x in list if condition]`
- **Uniqueness**: Handling duplicates (logic, not sets yet)

## What You'll Build
- `process_waitlist(schedule, waitlist)`
- `add_emergency(schedule, appointment)`
- `clean_duplicates(schedule)`
- `generate_report(schedule)`

## Prerequisites
- Completed Lab 2

## How to Use This Lab
1. **Read** `README.md`
2. **Study** `tasks.md` (pay attention to edge cases)
3. **Start** with `starter_code.py`
4. **Implement** tasks robustness
5. **Run** `tests.py`

## Task Summary
- Task 1: Process Waitlist (Batch)
- Task 2: Emergency Insert (Priority)
- Task 3: Deduplicate (Optimization)
- Task 4: Analytics Report (Transformation)

## Time Estimate
- Reading: 20 minutes
- Implementation: 120-150 minutes
- Testing: 30 minutes
- **Total**: 3-4 hours

## Key Concepts Practiced
- `.extend()` vs loop append
- `.insert(0, item)` performance implications
- `[f"{i}: {appt}" for i, appt in enumerate(L)]`
