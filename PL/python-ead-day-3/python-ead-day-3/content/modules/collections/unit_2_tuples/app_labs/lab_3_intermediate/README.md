---
title: "Self-Documenting Records"
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 3
difficulty: intermediate
use_case: clinical_diagnostics
domain: healthcare
order: 3
duration_hours: 2
tags:
  topics: ["collections", "tuples"]
  subtopics:
    - namedtuple
    - structured-data
---

# Lab 3: Self-Documenting Records

**Module**: Collections
**Objective**: Use the `namedtuple` factory from the `collections` module to improve code legibility.
**Difficulty**: Intermediate
**Context**: Clinical Diagnostics

## Generic Information
**Problem Statement**: Reading `patient[1]` or `vitals[0]` is confusing for new developers. What is index 1? What is index 0? We need the immutability of a tuple with the readability of an object.
**Goals**:
- Define a `NamedTuple` for a Lab Result.
- Access data by name (e.g., `result.value`) instead of index.

## Use Case
**Title**: Lab Report Generation
**Description**: Stores a lab test result with a Name, Value, and Unit (e.g., "Glucose", 95, "mg/dL").

### Rules
- Import `namedtuple` from `collections`.
- Define a type named `LabResult`.
- Use dot notation to access attributes.

### Test Cases
- Case 1: Create a `LabResult`, verify name and value access.
- Case 2: Ensure the record is still immutable (reassignment fails).

### Success Criteria
- Code is significantly more readable than standard index-based tuples.
