---
title: Appointment Scheduling - Part 2
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 2
difficulty: intermediate
use_case: appointment_scheduling
domain: healthcare
order: 2
duration_hours: 3
tags:
  topics: ["lists", "collections"]
  subtopics:
    - sorting
    - filtering
    - removing
    - searching
---

# Lab 2 (Intermediate): Appointment Scheduling - Part 2

**Module**: Collections
**Objective**: specific focus on modifying and organizing list data
**Difficulty**: Intermediate
**Context**: Healthcare

## Generic Information
**Problem Statement**: The clinic needs to organize the daily appointment list, remove cancelled ones, and sort them by time.
**Goals**:
- Clean up the appointment list
- Sort appointments chronologically
- Find specific appointments
- Generate a formatted view
**Data Elements**: Appointment Strings (e.g., "10:00 - John Doe")

## Use Case
**Title**: Daily Schedule Organizer
**Description**: A system to process a raw list of appointment strings, removing invalid entries and sorting them.
**Rules**:
- Appointments format: "HH:MM - Patient Name"
- Cancelled appointments must be removed.
- Final list must be sorted by time.

### Test Cases
- Case 1: Cancel specific appointment (Remove value)
- Case 2: Sort unordered list of times
- Case 3: Filter out slots outside business hours (09:00 - 17:00)

### Success Criteria
- Code correctly removes items without crashing
- sorting creates correct chronological order
- Slicing extracts correct time ranges

## Overview
In Part 1, you learned to add items. Now, you will learn to **organize** them. Real-world data is messy. Patients cancel, doctors slot people in randomly. Your job is to take a chaotic list and turn it into a clean, sorted schedule.

## Learning Goals
- **Modify in-place**: Using `.remove()` and `.sort()`
- **Filtering**: Creating new lists without specific items
- **Slicing**: Extracting parts of the schedule
- **Searching**: Finding if a patient exists

## The Scenario
The receptionist has a digital scratchpad where they type in appointments as they come in.
`["14:00 - Smith", "09:00 - Doe", "12:00 - Jones"]`
It's a mess. They also need to delete an appointment when someone calls to cancel.

You need to build the "Organizer" feature that:
1.  Takes this raw list.
2.  Removes cancelled patients.
3.  Sorts it by time (strings sort alphabetically, which works for 24h ISO time!).
4.  Prints the morning shift (09:00 - 12:00) separately.

## What You'll Build
- `cancel_appointment(schedule, appointment_str)`
- `organize_schedule(schedule)`
- `get_morning_shift(schedule)`

## Prerequisites
- Completed Lab 1

## How to Use This Lab
1. **Read** `README.md`
2. **Study** `tasks.md`
3. **Start** with `starter_code.py`
4. **Implement** tasks
5. **Run** `tests.py`

## Task Summary
- Task 1: Cancel Appointment (Remove)
- Task 2: Sort Schedule (Order)
- Task 3: Filter Business Hours (Conditionals)
- Task 4: Get Morning Shift (Slicing)

## Time Estimate
- Reading: 15 minutes
- Implementation: 90-120 minutes
- Testing: 30 minutes
- **Total**: 2-3 hours

## Key Concepts Practiced
- `list.remove()` vs `del`
- `list.sort()`
- List Slicing `[start:end]`
- Iteration logic

## Common Pitfalls
- **Modifying while iterating**: Creating a loop to remove items usually causes bugs (skipping items).
- **Sort returns None**: Remember `my_list.sort()` changes the list in-place and returns `None`. Don't do `new_list = old.sort()`.

## Next Steps
After Lab 2:
1. Proceed to Lab 3 (Advanced) for complex processing and list comprehensions.
