---
title: "The Clinical Trial"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 5
difficulty: advanced
use_case: inheritance-abstraction
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["abc", "inheritance", "super"]
---

# Lab 5: The Clinical Trial

**Module**: Thinking in Objects
**Objective**: Use inheritance and ABCs to model different phases of a clinical trial.
**Difficulty**: Advanced
**Context**: Research & Development

## Problem Statement
A `TrialPhase` is an abstract concept. 
- Phase 1 tests Safety.
- Phase 2 tests Efficacy.
- Phase 3 tests Comparison.

Specific phases share some logic (e.g., enrolling patients) but differ in their `evaluate_results()` method.

## Requirements
1.  **Abstract Base**: `TrialPhase(ABC)`.
    - `enroll(count)`: Increases `self.participants`.
    - Abstract `evaluate()`: Returns a string status.
2.  **Concrete Classes**:
    - `Phase1Safety`: `evaluate` returns "Safety Passed" if participants > 10.
    - `Phase2Efficacy`: `evaluate` returns "Efficacy Verified" if participants > 50.
3.  **Use of `super()`**:
    - Child classes should call `super().__init__(name)` to set the phase name.

## Expected Output
```text
Phase 1: Safety Passed
Phase 2: Insufficient Data (Efficacy Failed)
```
