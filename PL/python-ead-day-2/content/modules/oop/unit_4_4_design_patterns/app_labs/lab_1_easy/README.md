---
title: "System Config - Singleton Pattern"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 1
difficulty: easy
use_case: global_system_settings
domain: healthcare
order: 1
duration_hours: 0.75
tags:
  topics: ["oop", "design-patterns", "singleton"]
  subtopics:
    - single-instance
    - global-state
    - object-lifecycle
---

# Lab 1: Global Configuration Singleton

## Overview
In the MedGuard system, every sensor and monitor must refer to the same set of safety thresholds (e.g., minimum heart rate). If different components used different configurations, it would lead to inconsistent alerts.

## Use Case: System Safety Settings
You will create a `SystemConfig` class. No matter how many times you "create" a config object in different parts of the code, it should always return the exact same instance.

## Lab Structure
- `SystemConfig`: The Singleton class managing alert thresholds.
- Validation: Verifying object IDs are identical across the application.
