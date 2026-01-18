---
title: "Treatment Plan Management - Advanced Validation"
type: app_lab
module: oop
unit: unit_3_3_properties_and_encapsulation
lab_number: 5
difficulty: advanced
use_case: treatment_plan_management
domain: healthcare
order: 5
duration_hours: 3.5
tags:
  topics: ["oop", "properties", "validation"]
  subtopics:
    - dependent-properties
    - complex-validation
    - date-handling
---

# Lab 5: Treatment Plan Management

**Objective**: Implement complex validation logic and dependent properties.
**Difficulty**: Advanced

## Use Case
Manage a patient's treatment plan. A plan has a start date, end date, medication, and daily dosage. 
- End date must be after start date.
- Dosage must be positive and within safe limits for the medication type.
- Duration is a calculated property (end - start).
- Changes to dates automatically update duration.

## Task Summary
- **Task 1**: Date Validation (end > start)
- **Task 2**: Dependent Property `duration_days`
- **Task 3**: Daily Dosage Validation based on generic limits
- **Task 4**: `total_dosage` computed property (duration * daily)
- **Task 5**: `is_active` property based on current date
