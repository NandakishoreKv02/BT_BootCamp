---
title: "Tuple Unpacking & Swapping"
type: app_lab
module: collections
unit: unit_2_tuples
lab_number: 2
difficulty: easy
use_case: patient_vitals
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["collections", "tuples"]
  subtopics:
    - unpacking
    - value-swapping
---

# Lab 2: Tuple Unpacking & Swapping

**Module**: Collections
**Objective**: Use tuple structures to move multiple pieces of data efficiently.
**Difficulty**: Easy
**Context**: Patient Vitals

## Generic Information
**Problem Statement**: When a machine reads vitals, it often returns them as a group (e.g., Temperature, Pulse). We need to "unpack" these values into individual variables for the user interface.
**Goals**:
- Unpack a vitals tuple into named variables.
- Practice the Pythonic way to swap two values using tuples.

## Use Case
**Title**: Vitals Processing
**Description**: A vitals sensor returns `(37.5, 72)`. We need to assign these to `temp` and `pulse`.

### Rules
- Use multi-variable assignment (`a, b = tuple`).
- Avoid using index numbers where unpacking is cleaner.

### Test Cases
- Case 1: Unpack a 3-item tuple into 3 variables.
- Case 2: Swap two floor numbers using tuple syntax.

### Success Criteria
- Demonstrated clean, readable data extraction from tuples.
