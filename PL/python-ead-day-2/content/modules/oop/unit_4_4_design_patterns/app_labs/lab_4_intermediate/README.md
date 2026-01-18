---
title: "Diagnosis Engine - Strategy Pattern"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 4
difficulty: intermediate
use_case: clinical_decision_support
domain: healthcare
order: 4
duration_hours: 1.0
tags:
  topics: ["oop", "design-patterns", "strategy"]
  subtopics:
    - algorithm-swapping
    - behavioral-design
    - interchangeable-logic
---

# Lab 4: Patient Analysis Strategy

## Overview
A heart rate of 110 bpm is "Normal" for an infant but "High" for an adult. Instead of having a massive `if/else` block in your monitor, you should use the **Strategy Pattern** to plug in a different comparison algorithm based on who is being monitored.

## Use Case: Demographic Analyzers
You will build a system where a `RiskAnalyzer` delegates its scoring logic to either an `AdultRiskStrategy` or a `PediatricRiskStrategy`.

## Lab Structure
- `RiskStrategy`: Base abstract class for algorithms.
- `AdultStrategy` & `PediatricStrategy`: Specific threshold logic.
- `PatientRiskAssessor`: The context class that uses a strategy.
