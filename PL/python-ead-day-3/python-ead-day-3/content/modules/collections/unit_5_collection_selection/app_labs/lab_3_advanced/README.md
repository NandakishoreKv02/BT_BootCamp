---
title: "Critical Care: Multi-Collection Monitoring"
type: app_lab
module: collections
unit: unit_5_collection_selection
lab_number: 3
difficulty: advanced
use_case: patient_monitoring_system
domain: healthcare
order: 3
duration_hours: 5
tags:
  topics: ["selection", "integration"]
  subtopics:
    - nested-collections
    - big-o
    - conversion-logic
    - data-protection
---

# Lab 3 (Advanced): Critical Care: Multi-Collection Monitoring

## Generic Information
**Problem Statement**: A Critical Care Unit (CCU) monitor needs to manage disparate types of data: instantaneous vitals, historical trends, and unique visit registries. Choosing the wrong collection for any of these will result in either lagging updates or data loss.

**Goals**:
- Implement high-speed lookup for current patient status.
- Maintain a chronological timeline of heart rates.
- Ensure a master registry of unique patients seen in a 24-hour window.
- Create immutable snapshots of system configurations for audit logs.

**Data Elements**:
- `vitals_history`: List of Tuples `(timestamp, bpm)`.
- `current_status`: Dictionary `{patient_id: status_string}`.
- `daily_registry`: Set of `patient_ids`.
- `config`: Frozenset of `active_device_ids`.

## Use Case
**Title**: Integrated CCU Monitoring
**Description**: Build a manager class or set of functions that handles these four distinct data needs using the most efficient structure for each. Demonstrate that lookups are O(1) and historical data remains ordered.

### Rules
- Vitals MUST be added in order.
- Current status lookups MUST be O(1).
- Registry MUST automatically prevent duplicates.
- System config MUST be immutable (protected from accidental change).

### Test Cases
- Case 1: Vitals history preserves exact order of addition.
- Case 2: Multi-patient lookup remains fast regardless of count.
- Case 3: Adding a patient twice to the registry results in only one entry.
- Case 4: Attempts to modify the config frozenset raise a TypeError.

### Success Criteria
- [ ] Dictionary used for status.
- [ ] List used for timeline.
- [ ] Set used for registry.
- [ ] Frozenset used for config.

## Overview
This advanced lab synthesizes everything learned about collection selection. It forces the developer to think about *why* a specific structure is chosen based on the Big O properties and mutability rules.

## How to Use This Lab
1. Analyze the four data requirements in `tasks.md`.
2. Map each requirement to the correct Python collection.
3. Implement the system in `starter_code.py`.
4. Verify with `tests.py`.
