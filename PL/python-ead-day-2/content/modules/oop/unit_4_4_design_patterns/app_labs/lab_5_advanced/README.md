---
title: "Treatment Protocols - Compound Patterns"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 5
difficulty: advanced
use_case: automated_medical_protocols
domain: healthcare
order: 5
duration_hours: 1.25
tags:
  topics: ["oop", "design-patterns", "factory", "strategy"]
  subtopics:
    - pattern-integration
    - dynamic-logic-selection
    - protocol-execution
---

# Lab 5: Dynamic Treatment Protocol Engine

## Overview
When a patient has a "Cardiac" event, the system should automatically load the "Cardiac Algorithm" (Strategy). This lab combines the **Factory** (to find the right algorithm) with the **Strategy** (to execute it).

## Use Case: Automated Protocol Loading
The system receives a condition string (e.g., "TRAUMA"). The `ProtocolFactory` returns the correct `TreatmentStrategy`.

## Lab Structure
- `TreatmentStrategy`: Interface for protocols.
- `CardiacStrategy`, `TraumaStrategy`: Specific protocols.
- `ProtocolFactory`: Returns a strategy based on a string.
- `PatientManager`: Stores the active strategy and executes it.
