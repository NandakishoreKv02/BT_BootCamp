---
title: "Dynamic Slot Management"
type: app_lab
module: collections
unit: unit_1_lists
lab_number: 2
difficulty: easy
use_case: appointment_scheduling
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["collections", "lists"]
  subtopics:
    - remove
    - pop
    - insert
---

# Lab 2: Dynamic Slot Management

**Module**: Collections
**Objective**: Practice modifying list content using removal and insertion methods.
**Difficulty**: Easy
**Context**: Appointment Scheduling

## Generic Information
**Problem Statement**: Patients might cancel appointments, or emergency walk-ins might need to be squeezed into the front of the line.
**Goals**:
- Remove a patient from the list.
- Insert an emergency patient at a specific position.
- "Serve" the first patient in line.

## Use Case
**Title**: Line Adjustments
**Description**: A patient cancels their 2:00 PM slot. An emergency arrives and is placed at the very top (index 0).

### Rules
- Use `.remove(name)` for cancellations.
- Use `.insert(index, name)` for walk-ins.
- Use `.pop(0)` to serve the next patient.

### Test Cases
- Case 1: Insert "EMERGENCY" at index 0, verify order.
- Case 2: Remove a name, verify list length decreases.

### Success Criteria
- The list reflects the dynamic changes of a real-world clinic queue.
