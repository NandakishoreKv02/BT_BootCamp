---
title: "Integrated Clinic Record"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 7
difficulty: expert
use_case: patient_records
domain: healthcare
order: 7
duration_hours: 3
tags:
  topics: ["oop", "integration"]
  subtopics:
    - data-structures
    - validation
    - production-quality
---

# Lab 7: Integrated Clinic Record

**Module**: Object-Oriented Programming - Part 1
**Objective**: Combine attributes, class variables, and basic input handling into a professional record system.
**Difficulty**: Expert
**Context**: Electronic Health Records (EHR)

## Generic Information
**Problem Statement**: We need one single, robust `Patient` class that can handle diverse data including contact lists, vitals history (nested data), and global facility information.
**Goals**:
- Use lists and dictionaries as instance attributes.
- Maintain global state.
- Ensure all attributes are correctly initialized.
**Data Elements**:
- `name`
- `contact_numbers` (List)
- `vitals_history` (Dictionary)
- `facility` (Class Variable)

## Use Case
**Title**: Comprehensive Patient Data System
**Description**: Managing a record that contains a list of emergency contacts and a dictionary of vitals (e.g., {"heart_rate": 72}).

### Rules
- `contact_numbers` must be initialized as an empty list if not provided.
- `vitals_history` must be initialized as an empty dictionary.

### Test Cases
- Case 1: Create patient, add a contact to the list, verify it is stored.
- Case 2: Update a vital in the dictionary, verify retrieval.

### Success Criteria
- The class handles nested data structures (lists/dicts) within the object state flawlessly.

## Overview
This final expert lab brings all concepts together into a system that looks exactly like a real backend data model.

---
