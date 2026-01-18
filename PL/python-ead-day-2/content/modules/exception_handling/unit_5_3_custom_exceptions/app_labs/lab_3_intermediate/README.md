---
title: "Clinic Management - Exception Hierarchy"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 3
difficulty: intermediate
use_case: error_hierarchy
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["exceptions", "hierarchy", "inheritance"]
  subtopics:
    - base-classes
    - granular-catching
---

# Lab 3: Clinic Management - Exception Hierarchy

**Objective**: Create a tiered exception hierarchy to manage different types of clinic operation failures (e.g., Scheduling and Billing) while allowing a single "catch-all" for general clinic errors.

## Generic Information
**Problem Statement**: Large applications often have many specific error types. Instead of catching 10 different exceptions separately, you can group them under a common parent. This allows you to handle general clinic failures in one place, while still being able to catch specific issues like `InsuranceExpiredError` when needed.
**Goals**:
- Define a base `ClinicError`.
- Define two child classes: `SchedulingError` and `BillingError`.
- Implement a controller that simulates these failures.
- Demonstrate catching the base class to handle both children.

## Use Case: Error Hierarchy
The "HealthSys" dashboard needs to report any operational failure in the clinic. If the scheduling fails or billing fails, it should show a general "Clinic operation failed" alert, but log the specific details.

## Lab Structure
1.  **Hierarchy Definition**: Creating the base and child classes.
2.  **Service Logic**: Functions that raise specific errors.
3.  **Controller**: A centralized handler that catches the base class.

## Getting Started
Remember that `except BaseClass` will catch any instance of a `ChildClass` that inherits from it.
