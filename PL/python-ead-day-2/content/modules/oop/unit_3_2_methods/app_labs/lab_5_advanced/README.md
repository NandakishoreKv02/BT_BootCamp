---
title: "Clinical Utility Suite"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 5
difficulty: advanced
use_case: clinical_math
domain: healthcare
order: 5
duration_hours: 3
tags:
  topics: ["oop", "static-methods"]
  subtopics:
    - static-methods
    - pure-functions
    - namespacing
---

# Lab 5: Clinical Utility Suite

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master static methods for grouping logic that doesn't depend on state.
**Difficulty**: Advanced
**Context**: Clinical Mathematics

## Generic Information
**Problem Statement**: Doctors often need to perform quick calculations, such as BMI or Age-based dosage adjustments. These calculations use general formulas that don't need a specific patient object to function.
**Goals**:
- Implement calculation tools as static methods.
- Group these tools logically within the `Patient` or a `HealthUtils` class.

## Use Case
**Title**: Medical Calculator
**Description**: Provide a standard way to calculate BMI: `weight / (height^2)`.

### Rules
- Use the `@staticmethod` decorator.
- Methods should handle edge cases (like zero height) to avoid crashes.

### Test Cases
- Case 1: Calculate BMI for 70kg and 1.75m.
- Case 2: Handle height = 0 gracefully.

### Success Criteria
- Static methods are accessible without instantiating an object.

## Overview
Learn to use `@staticmethod` to keep your namespace clean and organize functions that are logically related to patients but are "pure" in nature.

---
