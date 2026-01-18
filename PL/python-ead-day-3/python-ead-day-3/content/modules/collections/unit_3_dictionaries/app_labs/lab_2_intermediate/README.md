---
title: Doctor Schedule Management
type: app_lab
module: collections
unit: unit_3_dictionaries
lab_number: 2
difficulty: intermediate
use_case: doctor_schedule_management
domain: healthcare
order: 2
duration_hours: 3
tags:
  topics: ["dictionaries", "collections"]
  subtopics:
    - nested-dictionaries
    - dict-methods
    - filtering
    - aggregation
---

# Lab 2 (Intermediate): Doctor Schedule Management

**Module**: Collections
**Objective**: specific focus on nested dictionaries and data aggregation
**Difficulty**: Intermediate
**Context**: Healthcare

## Generic Information
**Problem Statement**: The clinic needs to manage doctor schedules, assigning patients to specific slots and tracking availability by specialty.
**Goals**:
- Manage complex nested data structures (doctors -> schedule -> days)
- Assign patients to specific time slots
- Search for doctors by specialty
- Generate availability reports
**Data Elements**: Doctor ID, Name, Specialty, Schedule (Date -> Slots -> Patient ID)

## Use Case
**Title**: Doctor Scheduling System
**Description**: A system to manage doctor profiles and their daily appointment schedules.
**Rules**:
- Doctor IDs are unique integers.
- Each doctor has a specialty (e.g., "Cardiology", "Pediatrics").
- Schedules are dictionaries mapped by date string (e.g., "2023-10-27").
- A slot can hold one Patient ID (or None if empty).

### Test Cases
- Case 1: Add new doctor with empty schedule
- Case 2: Assign patient to specific slot (handling nested keys)
- Case 3: Find all doctors with specialty "Cardiology"
- Case 4: Calculate total patients for a doctor

### Success Criteria
- Nested dictionary structure is maintained correctly
- Patient assignments don't overwrite existing bookings without check
- Search returns correct list of doctors
- Reports result in accurate counts

## Overview
Moving beyond simple key-value pairs, this lab challenges you to work with **nested dictionaries**. Real-world data is rarely flat; it has layers. Here, you'll manage a database of doctors where each doctor has their own inner dictionary representing their schedule.

## Learning Goals
- Manipulate **nested dictionaries** (accessing `dict[key][inner_key]`)
- Perform **filtering** on dictionary values
- **Update** deeply nested data safely
- **Aggregate** data from multiple dictionary entries

## The Scenario
"City Health Clinic" has multiple doctors with different specialties. The current system is just a list of names. They need a way to track *who* is working *when* and *which patients* they are seeing.

You need to build a system that can:
1.  Register a doctor and their specialty.
2.  Open up appointment slots for a specific date.
3.  Book a patient into a slot.
4.  Tell management how many patients a doctor is seeing.

## What You'll Build
A simpler version of a scheduling engine using:
- `doctors_db`: A master dictionary of doctor records.
- Functions to manipulate this deep structure.

## Prerequisites
- Completed Lab 1 (Basic Dictionaries)
- Comfortable with lists inside dictionaries and dictionaries inside dictionaries.

## How to Use This Lab
1. **Read** `README.md` for context
2. **Study** `tasks.md` for detailed requirements
3. **Start** with `starter_code.py`
4. **Implement** tasks, considering edge cases (missing dates, full slots)
5. **Run** `tests.py` frequently
6. **Check** `solution/solution.py` if stuck

## Task Summary
- Task 1: Register Doctor (Nested Structure Setup)
- Task 2: Manage Schedule Slots (Adding nested keys)
- Task 3: Book Appointment (Deep update)
- Task 4: Search by Specialty (Filtering)
- Task 5: Workload Report (Aggregation)

## Time Estimate
- Reading: 15 minutes
- Implementation: 90-120 minutes
- Testing: 30 minutes
- **Total**: 2-3 hours

## Key Concepts Practiced
- Nested dictionary access `db[id]["schedule"][date]`
- Iterating through dictionary values
- Conditional filtering
- accumulating counts

## Common Pitfalls
- **KeyError on Nested Access**: Trying to access `schedule["2023-01-01"]` before that date key exists. You often need to check existence or use `.setdefault()`.
- **Reference Issues**: Remember that modifying a dictionary inside a function modifies the original (mutable).

## Next Steps
After Lab 2:
1. You'll be ready for Lab 3 (Advanced Analytics)
2. Consider how to handle "Time" within dates (maybe another layer of nesting?)
