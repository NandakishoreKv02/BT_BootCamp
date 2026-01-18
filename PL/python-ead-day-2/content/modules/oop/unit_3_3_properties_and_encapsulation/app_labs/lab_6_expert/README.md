---
title: "Critical Care Unit - Production System"
type: app_lab
module: oop
unit: unit_3_3_properties_and_encapsulation
lab_number: 6
difficulty: expert
use_case: critical_care_management
domain: healthcare
order: 6
duration_hours: 4.5
tags:
  topics: ["oop", "production", "encapsulation"]
  subtopics:
    - audit-logging
    - aggregation
    - strict-validation
    - collection-management
---

# Lab 6: Critical Care Unit Management

**Objective**: Build a production-ready class managing a collection of objects with strict encapsulation.
**Difficulty**: Expert

## Use Case
Manage a Critical Care Unit (CCU) containing multiple patients.
- The list of patients must be strictly protected; direct access prohibited.
- Adding/removing patients goes through methods that validate and log the action.
- Changing unit settings (e.g., `max_capacity`) logs the change.
- Aggregate stats (e.g., `occupancy_rate`, `average_acuity`) are computed live.

## Task Summary
- **Task 1**: Encapsulated Collection Management (add/remove methods, protected list)
- **Task 2**: Audit Logging System (log changes to capacity or patient list)
- **Task 3**: Dynamic Aggregates (occupancy percent, list of critical patients)
- **Task 4**: Strict Setter Validation (capacity limits, patient object types)
- **Task 5**: Properties for API-like access (e.g., `is_full`, `available_beds`)
