---
title: "Audit Trail: Removing Log Noise"
type: app_lab
module: collections
unit: unit_5_collection_selection
lab_number: 2
difficulty: intermediate
use_case: audit_log_processing
domain: healthcare
order: 2
duration_hours: 3
tags:
  topics: ["selection", "manipulation"]
  subtopics:
    - dictionary-mapping
    - deduplication
    - sorting
---

# Lab 2 (Intermediate): Audit Trail: Removing Log Noise

## Generic Information
**Problem Statement**: The hospital's audit log captures every click. For a "Daily Summary," we only want to see the *last* activity of each user, sorted by ID. The current raw log is a messy list of tuples with duplicates.

**Goals**:
- Use a dictionary to keep only the latest entry for each user ID.
- Convert the dictionary items back to a list for sorting.
- Produce a clean, ordered report.

**Data Elements**:
- `raw_logs`: List of tuples `(user_id, timestamp, action)`.

## Use Case
**Title**: Generate Daily Activity Report
**Description**: Process a messy stream of logs. For each unique `user_id`, we only care about the most recent activity in the list. Finally, display these users in ascending order of their IDs.

### Rules
- If multiple logs exist for the same ID, the *last* one in the input list should overwrite previous ones.
- The final output must be a List of tuples, sorted by `user_id`.

### Test Cases
- Case 1: Overlapping IDs result in only one entry per user.
- Case 2: The *latest* entry (based on list order) is the one preserved.
- Case 3: Final output is sorted numerically by ID.

### Success Criteria
- [ ] Dictionary used for deduplication.
- [ ] Values extracted and converted back to list correctly.
- [ ] Final list is sorted.

## Overview
This lab demonstrates a common design pattern: using a Dictionary as an intermediate deduplication tool before converting back to a List for presentation.

## How to Use This Lab
1. Implement the log processing logic in `starter_code.py`.
2. Follow the "Dictionary-to-Sorted-List" transformation pipeline.
3. Verify with `tests.py`.
