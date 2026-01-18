---
title: "The Treatment Aggregator"
type: app_lab
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
lab_number: 6
difficulty: expert
use_case: complex-polymorphism-aggregation
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["polymorphism", "overriding", "object-aggregation", "workflow"]
---

# Lab 6: The Treatment Aggregator

**Module**: Thinking in Objects
**Objective**: Build a system that manages multiple diverse subclasses through a single polymorphic interface to calculate aggregated clinical metrics.
**Difficulty**: Expert
**Context**: Care Coordination

## Problem Statement
A patient's care plan consists of many different `Treatment` items. 
1.  **Base Class**: `Treatment` with a method `get_intensity_score()`.
2.  **Specialized Subclasses**:
    - `DrugTherapy`: Score is `dosage * 10`.
    - `ClinicalExercise`: Score is `duration_minutes / 2`.
3.  **Aggregator**: A `CarePlan` class that contains a list of `Treatment` objects and computes a `total_plan_intensity()` by calling the polymorphic method on each item.

## Requirements
1.  **Hierarchy**:
    - `Treatment` -> `DrugTherapy`.
    - `Treatment` -> `ClinicalExercise`.
2.  **Implementation**:
    - Correct method overriding for calculation logic.
3.  **Aggregation**:
    - `CarePlan` must hold a list and sum up the scores.

## Expected Output
```text
Care Plan for Alice:
- Treatment: Aspirin (Score: 20)
- Treatment: Rehab Walk (Score: 15)
Total Plan Intensity: 35
```
