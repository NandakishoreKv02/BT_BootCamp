---
title: "The Unified Clinical Data Harvester"
type: app_lab
module: thinking_in_objects
unit: unit_2_13_method_overloading
lab_number: 6
difficulty: expert
use_case: complex-argument-mixing
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["args", "kwargs", "defaults", "overloading", "mixing-arguments"]
---

# Lab 6: The Unified Clinical Data Harvester

**Module**: Thinking in Objects
**Objective**: Build a complex, multi-signature method that uses mandatory arguments, default arguments, `*args`, and `**kwargs` simultaneously to ingest clinical data.
**Difficulty**: Expert
**Context**: Data Integration Engine

## Problem Statement
A `DataHarvester` must be able to record "Events".
1.  **Mandatory**: `event_type` (e.g., "Surgery").
2.  **Default**: `severity` (defaults to 1).
3.  **Variable Positional (`*args`)**: Accepts a list of `affected_vitals`.
4.  **Variable Keyword (`**kwargs`)**: Accepts any number of metadata `tags`.

You must implement this using the correct Pythonic argument order.

## Requirements
1.  **Architecture**:
    - Class `DataHarvester`.
2.  **Implementation**:
    - `log_event(self, event_type, severity=1, *vitals, **tags)`:
      - Return a summary dictionary containing all processed groups.
3.  **Argument Order**:
    - Remember the mandatory rule: Positional -> Defaults -> *args -> **kwargs.

## Expected Output
```text
Event Summary:
- Type: Surgery (Severity 3)
- Vitals Tracked: ('HR', 'BP', 'SpO2')
- Metadata: {'surgeon': 'Smith', 'room': 101}
```
