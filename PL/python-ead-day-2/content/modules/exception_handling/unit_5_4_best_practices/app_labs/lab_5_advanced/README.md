---
title: "The Defensive Shield - Logic Checks"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 5
difficulty: advanced
use_case: bug_prevention
domain: healthcare
order: 5
duration_hours: 2.0
tags:
  topics: ["exceptions", "defensive-programming", "validation"]
  subtopics:
    - data-integrity
    - pre-conditions
---

# Lab 5: The Defensive Shield - Logic Checks

**Objective**: Apply defensive programming techniques to validate data *before* it reaches critical logic, reducing the reliance on "expensive" exception handling for predictable failures.

## Generic Information
**Problem Statement**: While EAFP is great for environmental errors (like files or network), it's often better to check business logic *before* acting (LBYL style for logic). For example, checking if a patient's age is negative should be a simple `if` check, not a `ValueError` catch inside a heavy calculation.
**Goals**:
- Implement a multi-stage validator.
- Clean up data before it hits the "Core Engine".
- Categorize errors into "Data Quality" (Simple check) vs "System Errors" (True exceptions).

## Use Case: Bug Prevention
A "MedicationScheduler" ensures that a dose interval isn't zero and the drug name isn't empty. These are "Data Quality" issues that should be caught before the complex scheduling algorithm runs.

## Lab Structure
1.  **Validator**: A function that returns a list of data errors.
2.  **Core Core**: The function that actually does the work (and raises exceptions on truly unexpected events).
3.  **Shield**: The wrapper that only allows "Clean" data through.

## Getting Started
Defensive programming: Check your assumptions at the door.
