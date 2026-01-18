---
title: "Immutability Foundations"
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 1
difficulty: easy
use_case: patient_id_management
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["collections", "tuples"]
  subtopics:
    - creation
    - immutability
---

# Lab 1: Immutability Foundations

**Module**: Collections
**Objective**: Understand how to store data that should never change.
**Difficulty**: Easy
**Context**: Patient ID Management

## Generic Information
**Problem Statement**: Certain data, like a Patient's Date of Birth and SSN, are immutable—they should never change throughout the life of a record. Using a list would be risky.
**Goals**:
- Create a tuple to store fixed patient data.
- Attempt to modify it and observe the error (understanding immutability).

## Use Case
**Title**: Secure Identity Record
**Description**: Store a patient's Name, DOB, and Blood Type in a single, unchangeable tuple.

### Rules
- Use parentheses `()` for creation.
- Demonstrate that items cannot be reassigned.

### Test Cases
- Case 1: Create a tuple, verify values are accessible by index.

### Success Criteria
- Data is correctly stored in a tuple and protected from accidental changes.
