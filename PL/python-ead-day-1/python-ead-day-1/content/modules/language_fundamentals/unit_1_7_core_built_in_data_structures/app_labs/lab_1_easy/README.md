---
title: "Emergency Room Queue"
type: app_lab
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
lab_number: 1
difficulty: easy
use_case: workflow_optimization
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["lists", "list-methods"]
  subtopics: ["queue", "append", "pop"]
---

# Lab 1: Emergency Room Queue

**Module**: Language Fundamentals  
**Objective**: Use a list to simulate a FIFO (First-In, First-Out) queue for an ER waiting room.  
**Difficulty**: Easy  
**Context**: Healthcare - Patient Flow Management

## Generic Information
**Problem Statement**: Patients arrive in the order of their name. You need to maintain this order. When the doctor is ready, the patient at the front of the line is seen.

**Goals**:
- Adding patients to a list.
- Removing patients in order.
- Checking how many remain.

## Use Case
**Title**: Waiting Room Manager  
**Description**: Handle arrivals and admissions.

### Rules
- `arrive_patient(queue, name)` -> append to end.
- `see_next_patient(queue)` -> remove and return the FIRST item (index 0). If empty, return `None`.
- `get_queue_length(queue)` -> return count.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
