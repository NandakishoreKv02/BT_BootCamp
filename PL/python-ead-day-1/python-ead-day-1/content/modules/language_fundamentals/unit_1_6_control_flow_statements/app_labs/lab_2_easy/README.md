---
title: "Appointment Reminder Generator"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 2
difficulty: easy
use_case: patient_notification
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["loops", "for-loops"]
  subtopics: ["notification", "automation"]
---

# Lab 2: Appointment Reminder Generator

**Module**: Language Fundamentals  
**Objective**: Iterate through a list of patients and generate reminder strings for each.  
**Difficulty**: Easy  
**Context**: Healthcare - Patient Communications

## Generic Information
**Problem Statement**: The clinic needs to send reminders. You have a list of names and a shared appointment time. You need to create a list of reminder messages.

## Use Case
**Title**: Batch Reminder Logic  
**Description**: Prefix each patient name with a custom message.

### Rules
- `generate_reminders(patient_names, time_str)`
- Input: `["Alice", "Bob"]`, `"10:00 AM"`
- Output: `["Reminder: Alice, your appointment is at 10:00 AM.", "Reminder: Bob, your appointment is at 10:00 AM."]`
- Use an f-string inside the loop.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
