---
title: "Patient Appointment Scheduler"
type: app_lab
module: language_fundamentals
unit: unit_1_12_hands_on_labs
lab_number: 3
difficulty: intermediate
use_case: scheduling
domain: healthcare
order: 3
duration_hours: 3
tags:
  topics: ["dictionaries", "file-io", "error-handling"]
  subtopics: ["scheduling", "persistence"]
---

# Lab 3: Patient Appointment Scheduler

**Module**: Language Fundamentals  
**Objective**: Build a complete appointment scheduling system with file persistence, conflict detection, and cancellation capabilities.  
**Difficulty**: Intermediate  
**Context**: Healthcare - Outpatient Clinic Management

## Requirements
1. Manage daily appointment slots (dictionary: time -> patient_name)
2. Book appointments with conflict checking
3. Cancel appointments
4. Display daily schedule
5. Save/load schedule from file
6. Handle errors gracefully

### Functions
- `create_schedule()`: Initialize empty schedule dict
- `book_appointment(schedule, time, patient_name)`: Book if available
- `cancel_appointment(schedule, time)`: Remove appointment
- `is_slot_available(schedule, time)`: Check availability
- `display_schedule(schedule)`: Show formatted schedule
- `save_schedule(schedule, filename)`: Write to file
- `load_schedule(filename)`: Read from file

## Expected Output
```
=== DAILY APPOINTMENT SCHEDULE ===
09:00 - John Doe
10:00 - [AVAILABLE]
11:00 - Jane Smith
14:00 - [AVAILABLE]
```
