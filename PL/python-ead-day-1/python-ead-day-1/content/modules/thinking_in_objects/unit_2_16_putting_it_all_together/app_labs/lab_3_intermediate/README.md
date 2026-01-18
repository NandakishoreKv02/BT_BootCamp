---
title: "The Ambulance Dispatcher"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 3
difficulty: intermediate
use_case: object-interaction
domain: healthcare
order: 3
duration_hours: 1
tags:
  topics: ["interaction", "dependency", "state"]
---

# Lab 3: The Ambulance Dispatcher

**Module**: Thinking in Objects
**Objective**: Model the interaction between two classes: an `Ambulance` and a `Dispatcher`.
**Difficulty**: Intermediate
**Context**: Emergency Services

## Problem Statement
An `Ambulance` has an ID and a status (Idle/Busy). A `Dispatcher` manages a fleet of ambulances. The Dispatcher needs to find an available ambulance and assign it to a call.

## Requirements
1.  **Class `Ambulance`**:
    - ID, Status (`available=True`).
    - Method `assign_mission()`: sets status to False.
    - Method `complete_mission()`: sets status to True.
2.  **Class `Dispatcher`**:
    - List of `fleet`.
    - Method `dispatch_to_emergency(location)`: Finds the first available ambulance, assigns it, and returns "Dispatched Unit X". If none, returns "No units available".

## Expected Output
```text
Dispatched Unit A-1 to Downtown.
Dispatched Unit A-2 to Uptown.
No units available.
Unit A-1 back in service.
Dispatched Unit A-1 to Suburbs.
```
