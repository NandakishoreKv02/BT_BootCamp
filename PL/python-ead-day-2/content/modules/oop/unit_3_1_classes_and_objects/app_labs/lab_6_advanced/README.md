---
title: "Duplicate vs Unique Patients"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 6
difficulty: advanced
use_case: data_de-duplication
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["oop", "logic"]
  subtopics:
    - object-identity
    - reference-vs-value
    - is-operator
---

# Lab 6: Duplicate vs Unique Patients

**Module**: Object-Oriented Programming - Part 1
**Objective**: Differentiate between objects that look the same vs objects that ARE the same.
**Difficulty**: Advanced
**Context**: Medical Records Auditing

## Generic Information
**Problem Statement**: Two Patient records might have the exact same name "John Doe". This doesn't mean they are the same person. One is a new object in memory, while another might be a duplicate or a reference.
**Goals**:
- Use the `is` operator and the `==` operator.
- Understand object references in memory.
**Data Elements**:
- `name`

## Use Case
**Title**: Identify Duplicate Records
**Description**: When checking the database, we found two records for "Mary Smith". We need to check if they are two separate objects or just two names for the same memory address.

### Rules
- Two separate instances with the same data are NOT the same object (`is` returns `False`).
- An instance assigned to a new variable IS the same object (`is` returns `True`).

### Test Cases
- Case 1: `p1 = Patient("A")`, `p2 = Patient("A")`. `p1 is p2` should be False.
- Case 2: `p3 = p1`. `p3 is p1` should be True.

### Success Criteria
- Demonstrated understanding of object memory references.

## Overview
This lab covers the subtle but critical difference between data equality and object identity.

---
