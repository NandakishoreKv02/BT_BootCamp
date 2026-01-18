---
title: "The Extensible Analytics Engine"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 5
difficulty: advanced
use_case: extensibility
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["extensibility", "abstraction", "analytics"]
---

# Lab 5: The Extensible Analytics Engine

**Module**: Thinking in Objects
**Objective**: Demonstrate **Extensibility** by building a medical research tool that can be extended with new statistical calculations without ever changing the core record-processing code.
**Difficulty**: Advanced
**Context**: Medical Research Analytics

## Problem Statement
Medical researchers need to analyze patient vitals. Today they need the **Average Body Temperature**. Tomorrow they will need the **Maximum Heart Rate**. Next week, they might need the **Standard Deviation of Glucose Levels**.

If we write separate functions for every single metric, we will create massive code duplication. Instead, we want to create an "Extensible" engine that takes a `Dataset` object and a "Calculation Module" (function) to perform any math required.

## Requirements
1.  **Encapsulation**: Create a `Dataset` object (dictionary) that holds a label and a list of numerical values.
2.  **Generic Interface**: Write an `analyze_dataset(dataset, calc_func)` function that serves as the core engine.
3.  **Extensible Modules**: Implement standalone calculation functions (e.g., `get_mean`, `get_max`) that can be used interchangeably by the engine.
4.  **Proof of Extension**: Add a new calculation (e.g., `get_range`) to show that the system handles new requirements seamlessly.

## Expected Output
```text
Analysis: Body Temp (C) | Result: 37.7
Analysis: Glucose (mg/dL) | Result: 95
```
(Notice how the same engine processes different data with different math rules.)
