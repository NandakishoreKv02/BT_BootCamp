---
title: "Monitoring Hub - Full Integration"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 6
difficulty: expert
use_case: patient_safety_orchestration
domain: healthcare
order: 6
duration_hours: 2.0
tags:
  topics: ["oop", "design-patterns", "integration"]
  subtopics:
    - singleton-config
    - observer-alerts
    - factory-reporting
    - strategy-analysis
---

# Lab 6: Full Monitoring Orchestration

## Overview
This is the final capstone for the Design Patterns unit. You will build the **MedGuard Core Engine**.

## Use Case: End-to-End Monitoring
The system needs to:
1.  Access a global configuration (**Singleton**).
2.  Receive vital readings.
3.  Choose the right analysis logic based on patient age (**Strategy**).
4.  If hazardous, notify the correct response teams (**Observer**).
5.  Generate a closing report (**Factory**).

## Lab Structure
You will integrate classes from previous labs into a single, cohesive `MedGuardSystem` object.
