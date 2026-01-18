---
title: "The Enterprise Diagnostic System"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 6
difficulty: expert
use_case: comprehensive-design
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["abc", "srp", "abstraction", "architecture", "comprehensive"]
---

# Lab 6: The Enterprise Diagnostic System

**Module**: Thinking in Objects
**Objective**: Design a comprehensive diagnostic imaging system that combines ABC contracts, SRP, and multi-layer abstraction to simulate an enterprise-grade medical platform.
**Difficulty**: Expert
**Context**: Radiology Information System (RIS)

## Problem Statement
Build a complete diagnostic imaging workflow:
1.  **Abstract Scanner Base**: All scanners (MRI, CT, Ultrasound) must inherit from an ABC and implement `capture_image()` and `get_cost()`.
2.  **SRP Components**:
    - `ImagingOrder`: Stores patient ID and scanner type.
    - `CostEstimator`: Calculates total cost based on scanner type.
    - `ReportGenerator`: Creates a final diagnostic summary.
3.  **Abstraction Layer**: A high-level `DiagnosticWorkflow` class that coordinates the entire process through a single `execute_scan()` method.

## Requirements
1.  **ABC Implementation**:
    - Abstract `Scanner` with `capture_image()` and `get_cost()`.
    - 3 Concrete scanners with different costs.
2.  **SRP Classes**:
    - Each component handles exactly one responsibility.
3.  **Workflow Orchestration**:
    - `DiagnosticWorkflow.execute_scan(order)` must:
      - Instantiate the correct scanner.
      - Capture the image.
      - Calculate the cost.
      - Generate and return a report.

## Expected Output
```text
=== Enterprise Diagnostic Platform ===
Executing Order #1001 for Patient P-555...

Scanner: MRI
Image: High-resolution soft tissue scan completed.
Cost Analysis: $1200
Report Generated: [MRI] P-555 - Image captured. Total: $1200

Process complete.
```
