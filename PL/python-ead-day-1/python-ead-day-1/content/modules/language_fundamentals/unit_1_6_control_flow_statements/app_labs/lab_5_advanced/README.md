---
title: "Hospital Queue Manager"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 5
difficulty: advanced
use_case: workflow_optimization
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["loops", "nested-logic"]
  subtopics: ["triage", "queue"]
---

# Lab 5: Hospital Queue Manager

**Module**: Language Fundamentals  
**Objective**: Build a multi-level queue processor that handles patients based on priority and specific ward capacity.  
**Difficulty**: Advanced  
**Context**: Healthcare - Hospital Management System (HMS)

## Generic Information
**Problem Statement**: Patients in the ER are queued. Some have "Urgent" status, others "Routine". You need to process the queue, but stop if you hit the capacity limit for a specific ward.

## Use Case
**Title**: Priority-Based Admission  
**Description**: Calculate which patients can be admitted given a capacity constraint.

### Rules
- `admit_patients(queue, capacity)`
- `queue` is a list of dicts: `[{"name": "X", "urgent": True}, ...]`
- Admittance logic:
  - Loop through patients.
  - If patient is `urgent`, count them as admitted.
  - If patient is NOT `urgent`, only admit them if current admitted count < `capacity`.
  - Once total admitted (urgent + routine) reaches 2x `capacity` (absolute hard limit), stop entire loop.
- Return a list of names of admitted patients.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
