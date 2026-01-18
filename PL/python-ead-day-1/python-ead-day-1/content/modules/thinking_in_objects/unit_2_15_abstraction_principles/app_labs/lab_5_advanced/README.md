---
title: "The Clinical Data Pipeline"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 5
difficulty: advanced
use_case: abstraction-layers
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["abstraction", "encapsulation", "api-design"]
---

# Lab 5: The Clinical Data Pipeline

**Module**: Thinking in Objects
**Objective**: Build a multi-layer abstraction system where high-level clinical methods hide complex data transformations.
**Difficulty**: Advanced
**Context**: Data Analytics

## Problem Statement
A `LabAnalytics` system needs to provide simple public methods like `get_average_glucose()`, but internally this requires fetching raw data, validating it, filtering outliers, and computing statistics. You must hide all this complexity behind a clean abstraction layer.

## Requirements
1.  **Public Interface (High-Level Abstraction)**:
    - `get_average_glucose()`: Returns a clean number.
2.  **Private Implementation (Hidden Complexity)**:
    - `_fetch_raw_data()`: Simulates getting raw readings from a database.
    - `_validate(data)`: Filters out invalid readings (e.g., negative values).
    - `_compute_mean(data)`: Mathematical calculation.
3.  **Encapsulation**:
    - All helper methods must be private (prefixed with `_`).
    - Only `get_average_glucose()` is exposed to users.

## Expected Output
```text
Analyzing glucose trends...
Average Glucose Level: 118.3 mg/dL
(Processed 4 valid readings from system)
```
