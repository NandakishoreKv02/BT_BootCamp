---
title: "Smart Patient Intake"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 2
difficulty: intermediate
use_case: patient_data_ingestion
domain: healthcare
order: 2
duration_hours: 2.5
tags:
  topics: ["oop", "methods"]
  subtopics:
    - class-methods
    - factory-pattern
    - string-parsing
    - data-serialization
---

# Lab 2: Smart Patient Intake

**Module**: Object-Oriented Programming - Part 1
**Objective**: Implement class methods as factory functions to handle multiple data formats.
**Difficulty**: Intermediate
**Context**: Patient Registration System

## Generic Information
**Problem Statement**: Clinical data arrives from various sources: manual entry, CSV uploads, and legacy database strings. The standard `__init__` constructor is too rigid to handle all these formats cleanly. We need alternative ways to create patient objects based on the input source.
**Goals**:
- Use `@classmethod` to create "factory methods".
- Parse raw data types (strings, dictionaries) into structured objects.
- Maintain a clean and DRY (Don't Repeat Yourself) constructor.
**Data Elements**:
- `name`: Patient's name.
- `age`: Patient's age (int).
- `condition`: Primary medical complaint.

## Use Case
**Title**: Multi-Format Registration
**Description**: The registration desk needs to handle a standard registration, a fast-track registration via a legacy string (e.g., "Alice:30:None"), and a bulk import via dictionaries.

### Rules
- `__init__` should handle individual arguments.
- `from_string` should parse "Name:Age:Condition" format.
- `from_dict` should extract values from keys `name`, `age`, and `condition`.

### Test Cases
- Case 1: Create from string "Bob:45:Cough".
- Case 2: Create from dictionary `{"name": "James", "age": 55, "condition": "Fever"}`.
- Case 3: Standard creation from variables.

### Success Criteria
- Factory methods return a new instance of the class.
- Data is correctly mapped to instance attributes.

## Overview
This intermediate lab moves beyond data processing to architectural patterns. You will learn how `@classmethod` allows a class to be flexible and "smart" about how it is created.

---
