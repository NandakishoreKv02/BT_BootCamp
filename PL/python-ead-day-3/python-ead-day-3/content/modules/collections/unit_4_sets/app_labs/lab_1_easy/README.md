---
title: "Hospital Registry: Daily Check-in"
type: app_lab
module: collections
unit: unit_4_sets
lab_number: 1
difficulty: easy
use_case: hospital_registry
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["sets", "collections"]
  subtopics:
    - creation
    - deduplication
    - methods-add
    - methods-discard
---

# Lab 1 (Easy): Hospital Registry: Daily Check-in

## Generic Information
**Problem Statement**: The hospital's daily log contains many duplicate entries because patients check in at multiple desks (Reception, Triage, Billing). We need to maintain a clean record of unique patient IDs for the day.

**Goals**:
- De-duplicate a list of incoming IDs.
- Safely add new patients as they arrive.
- Efficiently count unique daily visitors.

**Data Elements**: 
- `patient_id`: Unique integer assigned to each patient.
- `daily_log`: A set of these IDs.

## Use Case
**Title**: Register Unique Daily Patients
**Description**: Process a batch of visiting IDs to remove duplicates and provide a way to add new arrivals without creating errors if they are already present.

### Rules
- All patient IDs must be stored in a set to ensure uniqueness.
- Adding a patient who is already present should not cause an error.
- Removing a patient (e.g., if they were entered in error) should be done safely.

### Test Cases
- Case 1: Initializing from a list with duplicates results in a set of only unique values.
- Case 2: Adding a new ID increases the set size; adding an existing ID does not.
- Case 3: Removing an ID that exists works; removing one that doesn't does not crash.

### Success Criteria
- [ ] List converted to set correctly.
- [ ] No duplicates exist in the final registry.
- [ ] Registry count reflects unique individuals only.

## Overview
This lab covers the absolute fundamentals of Python sets: creating them from other sequences, adding items, and removing items safely.

## What You'll Build
You will create a set-based registry system for a hospital's daily intake desk.

## How to Use This Lab
1. Review `tasks.md` for specific function requirements.
2. Implement logic in `starter_code.py`.
3. Verify with `tests.py`.
