---
title: "The Electronic Health Record (EHR)"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 4
difficulty: intermediate
use_case: composition-vs-aggregation
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["composition", "aggregation", "lifecycle"]
---

# Lab 4: The Electronic Health Record (EHR)

**Module**: Thinking in Objects
**Objective**: distinguish between **Composition** (strong ownership) and **Aggregation** (weak link) within a single clinical system.
**Difficulty**: Intermediate
**Context**: EHR Data Modeling

## Problem Statement
In a medical record system:
1.  A **Patient** *always* has a **MedicalChart** which is private to them and destroyed if the record is expunged (Composition).
2.  A **Patient** is *associated* with a **PrimaryDoctor**, but the doctor exists independently of any one patient (Aggregation).

Your task is to implement this distinction in your `Patient` class.

## Requirements
1.  **Modeling**:
    - Build `MedicalChart` class.
    - Build `Doctor` class.
    - Build `Patient` class.
2.  **Implementation**:
    - In `Patient.__init__`, create a new `MedicalChart` object (Composition).
    - In `Patient.__init__`, accept an *existing* `Doctor` object (Aggregation).
3.  **Validation**:
    - Demonstrate that if you have two patients, each has their own unique Chart (Composition), but they can share the same Doctor (Aggregation).

## Expected Output
```text
Patient A: Chart ID 101, Doctor: Dr. Smith
Patient B: Chart ID 102, Doctor: Dr. Smith
```
