---
title: "Dynamic Config Loader"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 6
difficulty: expert
use_case: system_configuration
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["dynamic-typing", "reflection"]
  subtopics: ["type-inference", "configuration"]
---

# Lab 6: Dynamic Config Loader

**Module**: Language Fundamentals  
**Objective**: Build a configuration loader that infers data types from raw string values (converting "true" to bool, "123" to int), mirroring how frameworks like Flask handling `.env` files.  
**Difficulty**: Expert  
**Context**: Healthcare - System Configuration

## Generic Information
**Problem Statement**: You are building a healthcare SaaS platform. Configuration comes from environment variables (all strings). You need a utility that reads a dict of raw strings and returns a dict of properly typed Python objects.

**Goals**:
- Implement type inference logic.
- Handle edge cases (empty strings, "None").

## Use Case
**Title**: Type Inference Engine
**Description**:
Input:
```python
{
    "MAX_RETRIES": "5",
    "ENABLE_AUDIT": "true",
    "TIMEOUT": "30.5",
    "DB_NAME": "prod_db",
    "CACHE_TTL": "None"
}
```
Output:
```python
{
    "MAX_RETRIES": 5,          # int
    "ENABLE_AUDIT": True,      # bool
    "TIMEOUT": 30.5,           # float
    "DB_NAME": "prod_db",      # str
    "CACHE_TTL": None          # NoneType
}
```

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
