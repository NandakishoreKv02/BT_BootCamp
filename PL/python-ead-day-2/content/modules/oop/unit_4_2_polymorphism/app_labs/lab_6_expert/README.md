---
title: "Critical Alert System - Advanced Polymorphism"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 6
difficulty: expert
use_case: medical_device_interface
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["oop", "polymorphism", "strategy-pattern"]
  subtopics:
    - decoupling-alert-logic
    - dynamic-strategies
    - behavioral-polymorphism
---

# Lab 6: Critical Alert System - Advanced Polymorphism

**Objective**: Build a highly decoupled, polymorphic alerting system where different evaluation "strategies" can be plugged into a central monitoring engine.

## Generic Information
**Problem Statement**: Monitoring patients involves different rules for different vitals. For some (like Fever), a single high reading is bad. For others (like Heart Rate), we might care about the variability. We want a `Monitor` that can take any `AlertStrategy` and use it to evaluate data.
**Goals**:
- Define a polymorphic `AlertStrategy` interface.
- Implement `ThresholdStrategy` (alert if any value > limit).
- Implement `TrendStrategy` (alert if the average is increasing).
- Implement a `PatientMonitor` that executes these strategies.

## Use Case: Dynamic Monitoring
- **AlertStrategy (ABC)**: Polymorphic interface with `should_alert(data_list)`.
- **ThresholdStrategy**: Checks max(data) > target.
- **TrendStrategy**: Checks if the last average is higher than previous half.
- **PatientMonitor**: Orchestrates the evaluation.

## Lab Structure
1.  **AlertStrategy (ABC)**: The core contract.
2.  **Concrete Strategies**: Multiple ways to evaluate health data.
3.  **Monitor Class**: Composition-based class that uses the polymorphic strategies.
4.  **Integration**: Switch strategies dynamically at runtime.
