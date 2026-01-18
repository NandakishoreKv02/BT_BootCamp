---
title: "Smart Patient registration"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 4
difficulty: intermediate
use_case: data_entry
domain: healthcare
order: 4
duration_hours: 2.5
tags:
  topics: ["oop", "class-methods"]
  subtopics:
    - factory-pattern
    - alternative-constructors
    - parsing
---

# Lab 4: Smart Patient registration

**Module**: Object-Oriented Programming - Part 1
**Objective**: Use class methods to implement the Factory Pattern for alternative object creation.
**Difficulty**: Intermediate
**Context**: Data Management

## Generic Information
**Problem Statement**: The clinic receives patient data in various formats: individual fields, colon-separated strings from legacy systems, and dictionaries from web forms.
**Goals**:
- Implement a class method to create a patient from a string.
- Implement a class method to create a patient from a dictionary.

## Use Case
**Title**: Alternative Data Ingestion
**Description**: Support `Patient.from_string("John Doe:30")` and `Patient.from_dict({"name": "Jane", "age": 25})`.

### Rules
- Factory methods must return a new instance of the class.
- Handle malformed strings gracefully (optional for extra points).

### Test Cases
- Case 1: Create from string and verify attributes.
- Case 2: Create from dictionary and verify attributes.

### Success Criteria
- New objects are instantiated with correct data regardless of input source.

## Overview
This lab demonstrates the power of `@classmethod` for creating flexible "entry points" into your objects.

---
