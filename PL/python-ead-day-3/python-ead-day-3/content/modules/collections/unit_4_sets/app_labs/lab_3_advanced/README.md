---
title: "Staffing Compliance & Audit"
type: app_lab
module: collections
unit: unit_4_sets
lab_number: 3
difficulty: advanced
use_case: staffing_audit
domain: healthcare
order: 3
duration_hours: 5
tags:
  topics: ["sets", "collections"]
  subtopics:
    - subsets
    - disjoint-sets
    - frozensets
    - set-comprehensions
---

# Lab 3 (Advanced): Staffing Compliance & Audit

## Generic Information
**Problem Statement**: The hospital needs to audit ward staffing to ensure only authorized personnel are working on specific shifts. We also need to categorize shifts using immutable sets and extract specific staff groups using set comprehensions.

**Goals**:
- Verify if a current shift's staff are all from the authorized pool (Subset check).
- Ensure no overlaps between mutually exclusive teams (Disjoint check).
- Use `frozensets` to define immutable shift types.
- Efficiently extract subsets of staff based on criteria (Set comprehension).

**Data Elements**:
- `authorized_staff`: Master set of all hospital employee IDs.
- `ward_shift`: Set of IDs currently working in a specific ward.
- `REQUIRED_CERTIFICATIONS`: A `frozenset` of mandatory certification codes.

## Use Case
**Title**: Audit Ward Staffing
**Description**: Perform high-level set checks to ensure security and compliance, managing staff lists that must not overlap and verifying sub-groups.

### Rules
- If a `ward_shift` contains IDs not in `authorized_staff`, it must be flagged.
- Morning and Night teams must be disjoint (no person can work both).
- Use `frozenset` for data that should not change during the audit process.

### Test Cases
- Case 1: `issubset` correctly identifies unauthorized personnel.
- Case 2: `isdisjoint` identifies illegal double-shifts.
- Case 3: Set comprehension correctly filters staff by ID range or other criteria.

### Success Criteria
- [ ] Compliance violations (unauthorized staff) are detected.
- [ ] Scheduling conflicts (overlapping shifts) are identified.
- [ ] Performance-critical filtering is done via set comprehensions.

## Overview
This advanced lab combines complex set relationships (`issubset`, `isdisjoint`) with modern Python features like `frozensets` and comprehensions.

## How to Use This Lab
1. Define fixed requirements using `frozenset`.
2. Implement the audit functions using set comparison methods.
3. Validate with the provided comprehensive test suite.
