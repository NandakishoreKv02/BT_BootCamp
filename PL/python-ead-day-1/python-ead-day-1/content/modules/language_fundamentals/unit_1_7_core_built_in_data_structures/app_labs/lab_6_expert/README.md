---
title: "Hospital Hierarchy Mapper"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 6
difficulty: expert
use_case: resource_management
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["nesting", "sets", "dictionaries"]
  subtopics: ["organization", "deduplication"]
---

# Lab 6: Hospital Hierarchy Mapper

**Module**: Language Fundamentals  
**Objective**: Create a nested registry that maps Departments to Doctors, and Doctors to their unique set of specialties.  
**Difficulty**: Expert  
**Context**: Healthcare - HR & Scheduling System

## Generic Information
**Problem Statement**: Hospital data is hierarchical. A department (e.g. "Cardiology") has many doctors. Each doctor has multiple specialties (e.g. "Echo", "Surgery"). You need to build a system that prevents duplicate specialties for a doctor and duplicate doctors in a department.

## Use Case
**Title**: Professional Registry  
**Description**: Build and query a nested data structure.

### Structure
`{ "Department": { "Doctor_Name": {"Specialties_Set"} } }`

### Rules
- `register_doctor(registry, dept, doctor, specialty)`
  - Add specialty to a set for that doctor.
  - Set ensures no duplicates.
- `get_dept_doctors(registry, dept)` -> Return list of doctor names.
- `get_unique_specialties_for_dept(registry, dept)` -> Return a set of all specialties practiced by ALL doctors in that department.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
