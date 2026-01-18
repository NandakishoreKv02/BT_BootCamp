---
title: "The SRP Billing Refactor"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 3
difficulty: intermediate
use_case: srp-refactoring
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["srp", "design-principles", "refactoring"]
---

# Lab 3: The SRP Billing Refactor

**Module**: Thinking in Objects
**Objective**: Apply the Single Responsibility Principle (SRP) to refactor a "God Class" into modular, focused components.
**Difficulty**: Intermediate
**Context**: Financial Operations

## Problem Statement
A legacy class `PatientBillingOfficer` is doing too much. It stores the patient's data, calculates the total bill based on a list of services, and formats the output into a string. If the billing logic changes, or the data storage changes, we have to modify the same class. This violates SRP.

You must refactor this into three separate classes.

## Requirements
1.  **Refactor**:
    - `PatientProfile`: Stores `name` and a list of `services`.
    - `CostCalculator`: Has a method `calculate(services)` that returns the sum of prices.
    - `StatementRenderer`: Has a method `render(patient, total)` that returns a formatted string.
2.  **Implementation**:
    - Each class must have exactly one reason to change.

## Expected Output
```text
Rendering Statement...
Account: John Doe
Total Due: $450
```
