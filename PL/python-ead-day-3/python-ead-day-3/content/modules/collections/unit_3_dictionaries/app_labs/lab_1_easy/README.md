---
title: Patient Records Management - Part 1
type: app_lab
module: collections
unit: unit_3_dictionaries
lab_number: 1
difficulty: easy
use_case: patient_records_management
domain: healthcare
order: 1
duration_hours: 2
tags:
  topics: ["dictionaries", "collections"]
  subtopics:
    - key-access
    - dict-methods
    - adding-items
    - safe-access
---

# Lab 1 (Easy): Patient Records Management - Part 1

**Module**: Collections
**Objective**: Build a patient lookup system using dictionaries
**Difficulty**: Beginner
**Context**: Healthcare

## Generic Information
**Problem Statement**: Clinic receptionists need a fast way to find patient details using their ID.
**Goals**:
- Store patient data efficiently
- Retrieve records instantly by ID
- Handle missing patients gracefully
**Data Elements**: Patient ID (int), Name (str), Age (int), Blood Type (str)

## Use Case
**Title**: Patient Lookup System
**Description**: A system to store and retrieve patient records using their unique ID.
**Rules**:
- Patient IDs must be unique integers
- Patient data is stored as a dictionary
- Lookups must handle non-existent IDs
- Updates should modify existing records or create new ones

### Test Cases
- Case 1: Add new patient record
- Case 2: Retrieve existing patient by ID
- Case 3: specific handling for missing ID (return None or default)

### Success Criteria
- Patient added successfully
- Valid ID returns correct details
- Invalid ID returns "Not Found" message/object
- Code uses dictionary methods for safety

## Overview
This lab focuses on using Python dictionaries to manage simple key-value data. You will build a basic system to store patient records where the ID is the key and the patient details are the value.

These fundamental operations—Create, Read, Update—are the building blocks of any medical record system.

## Learning Goals
- Understand dictionary key-value structure
- Practice adding and updating items
- Implement safe data retrieval using `.get()`
- Apply dictionary concepts to patient data management

## The Scenario
The reception desk at "City Health Clinic" currently uses a paper logbook to find patient files. This is slow and error-prone. When a patient arrives, the receptionist has to scan down a list to find their ID.

Management wants technical solution: a simple digital lookup tool. When the receptionist types in a Patient ID (e.g., `1001`), the system should instantly display their name and vital details. If the ID doesn't exist, it should clearly say "Patient Not Found" instead of crashing.

Your job is to build the backend logic for this lookup system using Python dictionaries, which are perfect for this "ID-to-Record" mapping.

## What You'll Build
A set of functions to manage a `patients` database (dictionary):
- `add_patient()`: To register new people
- `get_patient()`: To find them by ID
- `update_patient_age()`: To keep records current

## How to Use This Lab
1. **Read** `README.md` (this file) for overview
2. **Review** `tasks.md` for specific requirements
3. **Start** with `starter_code.py`
4. **Implement** each task one by one
5. **Run** `tests.py` to verify each task
6. **Compare** your solution with `solution/solution.py`

## Task Summary
- Task 1: Create and Initialize Patient Database
- Task 2: Implement Add Patient Functionality
- Task 3: Implement Safe Patient Lookup
- Task 4: Update Patient Information

## Time Estimate
- Reading: 10 minutes
- Implementation: 60-90 minutes
- Testing & review: 15 minutes
- **Total**: 1.5-2 hours

## Key Concepts Practiced
- Dictionary initialization
- Key-Value insertion
- `.get()` method for safe access
- Modifying values by key

## Common Pitfalls
- **KeyError**: Accessing a missing key with brackets `[]` instead of `.get()`.
- **Overwriting**: Accidentally using the same ID for a different patient (dictionaries require unique keys).

## Next Steps
After completing Lab 1:
1. Review your solution against provided solution
2. Move on to Lab 2 to handle more complex records (nested dictionaries)
3. Consider how to handle duplicate names (which keys prevent)
