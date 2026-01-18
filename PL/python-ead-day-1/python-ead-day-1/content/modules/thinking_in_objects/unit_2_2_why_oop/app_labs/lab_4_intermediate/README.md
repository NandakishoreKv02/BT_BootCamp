---
title: "The Scalable Ward System"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 4
difficulty: intermediate
use_case: scalability
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["scalability", "polymorphism-concept", "data-driven"]
---

# Lab 4: The Scalable Ward System

**Module**: Thinking in Objects
**Objective**: Demonstrate **Scalability** by designing an admission system where different wards have unique rules that are managed through "Logic Objects" rather than hardcoded logic.
**Difficulty**: Intermediate
**Context**: Hospital Capacity Expansion

## Problem Statement
A hospital has different admission rules for different wards:
- **General**: Anyone can enter if there is space.
- **ICU**: Only "High Priority" patients can enter.
- **Pediatrics**: Only patients under 18 can enter.

In procedural code, the `admit()` function would be a giant nested `if/elif` block. Adding a new ward type (like "Geriatric") would require editing a core, complex function. This is not **Scalable**.

Your task is to use a "Policy Map" to route admission logic dynamically based on the Ward's type.

## Requirements
1.  **Policy Isolation**: Define separate functions for `general_policy`, `icu_policy`, and `peds_policy`.
2.  **Generic Admission Engine**: Create an `admit_to_ward` function that looks up the correct logic in a dictionary and executes it.
3.  **Future Proofing**: Add a new policy (e.g., "VIP") to prove that you can scale the system without editing the core engine.

## Expected Output
```text
Admitting John (High Priority) to ICU: True
Admitting Bob (Low Priority) to ICU: False
Final Occupancy: 1/5
```
(Notice how the core system handles diverse rules without knowing what those rules are.)
