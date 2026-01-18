---
title: "Healthcare Data Architect: Fast Patient Lookup"
type: app_lab
module: collections
unit: unit_5_collection_selection
lab_number: 1
difficulty: easy
use_case: patient_lookup_optimization
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["selection", "performance"]
  subtopics:
    - conversion
    - membership-testing
    - performance-optimization
---

# Lab 1 (Easy): Healthcare Data Architect: Fast Patient Lookup

## Generic Information
**Problem Statement**: The hospital's current system stores "Inactive Patient IDs" in a massive list. When searching for a patient during registration, the system lags because it must scan the entire list every time.

**Goals**:
- Measure the performance difference between List search and Set search.
- Convert the legacy list to a high-performance set for production use.
- Implement a search helper that utilizes the optimal structure.

**Data Elements**:
- `inactive_ids_list`: A legacy list of 100,000+ IDs.
- `target_id`: The ID being searched.

## Use Case
**Title**: Optimize Registration Lookup
**Description**: Refactor the registration module to stop using sequential list scans and switch to hash-based set lookups for "Banned" or "Inactive" IDs.

### Rules
- The conversion from list to set should happen only once at startup.
- The search function must always return a Boolean.

### Test Cases
- Case 1: Search for an ID present in the collection returns True.
- Case 2: Search for a missing ID returns False.
- Case 3: Performance test (conceptual) — set lookup should be effectively instant.

### Success Criteria
- [ ] List converted to Set correctly.
- [ ] Boolean lookup logic implemented.
- [ ] No more O(n) scans in the main search loop.

## Overview
This lab introduces the most common and high-impact collection selection: choosing a Set over a List for membership testing.

## How to Use This Lab
1. Implement the conversion logic in `starter_code.py`.
2. Write the optimized search function.
3. Validate with `tests.py`.
