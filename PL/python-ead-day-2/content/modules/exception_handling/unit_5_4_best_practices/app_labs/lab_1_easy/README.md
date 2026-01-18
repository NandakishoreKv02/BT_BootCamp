---
title: "The Pythonic Dictionary - EAFP"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 1
difficulty: easy
use_case: pythonic_patterns
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["exceptions", "eafp", "best-practices"]
  subtopics:
    - code-style
    - dictionary-access
---

# Lab 1: The Pythonic Dictionary - EAFP

**Objective**: Refactor look-ahead (LBYL) code into Pythonic (EAFP) code for patient data access.

## Generic Information
**Problem Statement**: You are working on a legacy module that uses `if key in dict` checks everywhere. While this works, it can be slower in some cases and is less atomic. In Python, we prefer to "just do it" and handle the failure.
**Goals**:
- Replace `if` checks with `try-except`.
- Ensure default values are returned on failure.

## Use Case: Pythonic Patterns
A "PatientRecordViewer" retrieves optional fields (like 'MiddleName'). Instead of checking if the field exists, it tries to access it and returns an empty string if it's missing.

## Lab Structure
1.  **LBYL Function**: The old style.
2.  **EAFP Refactor**: Implement the new style.
3.  **Benchmark Info**: Understanding why EAFP is preferred.

## Getting Started
EAFP: "Easier to Ask for Forgiveness than Permission".
LBYL: "Look Before You Leap".
