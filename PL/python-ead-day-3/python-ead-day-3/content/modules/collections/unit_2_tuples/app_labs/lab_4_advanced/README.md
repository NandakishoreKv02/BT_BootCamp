---
title: "Immutability and Nested Data"
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 4
difficulty: advanced
use_case: medical_research
domain: healthcare
order: 4
duration_hours: 3
tags:
  topics: ["collections", "tuples"]
  subtopics:
    - nested-tuples
    - data-integrity
---

# Lab 4: Immutability and Nested Data

**Module**: Collections
**Objective**: Understand the boundaries of immutability when nesting mutable types inside tuples.
**Difficulty**: Advanced
**Context**: Medical Research

## Generic Information
**Problem Statement**: In research, data integrity is paramount. While a tuple is immutable, what happens if we put a list inside it? We need to understand the "referential immutability" of tuples to avoid subtle bugs in our research datasets.
**Goals**:
- Create a nested tuple structure.
- Prove that the tuple itself cannot change, but mutable items inside it (like lists) CAN be modified.
- Discuss how to achieve "True" immutability using nested tuples.

## Use Case
**Title**: Raw Research Dataset
**Description**: A research study stores a Tuple of Observations. Each observation is a List of readings. We must understand that while we can't delete an observation, we could accidentally change a reading within it.

### Rules
- Attempting to change a reference in the tuple will fail.
- Changing an item in a nested list will succeed.

### Test Cases
- Case 1: Reassign index 0 of the tuple (fail).
- Case 2: Modify index 0 of the nested list (succeed).

### Success Criteria
- Demonstrated a clear understanding of shallow vs deep immutability.
