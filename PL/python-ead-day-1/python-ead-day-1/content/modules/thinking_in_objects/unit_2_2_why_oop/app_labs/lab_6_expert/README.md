---
title: "The HL7 Industry Simulator"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 6
difficulty: expert
use_case: industrial-standards
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["industry-standards", "hl7", "serialization"]
---

# Lab 6: The HL7 Industry Simulator

**Module**: Thinking in Objects
**Objective**: Build a simulator for the **HL7 (Health Level 7)** data standard using an Object-Oriented approach. Experience why enterprise standards require structured objects to function at scale.
**Difficulty**: Expert
**Context**: Interoperability (System-to-System Mapping)

## Problem Statement
When Hospital A sends data to Hospital B, they use the **HL7** standard. An HL7 message is a long string composed of "Segments" (e.g., `PID` for Patient ID, `OBX` for Observation).
`PID|1|JOHN DOE|19800101`

In procedural code, building these messages involves messy string concatenation and complex loops. In OOP, we treat each segment as an object and the message as a container. This makes the code much cleaner and easier to validate.

## Requirements
1.  **Component Architecture**:
    - `create_segment(type, fields)` returns a Segment object (dictionary).
    - `create_message()` returns a Message container with an empty list of segments.
2.  **Assembly**: Create an `add_segment` function to link parts together.
3.  **Serialization**: Implement `to_hl7_string(message)` that converts the complex object structure back into the raw industrial string format using pipe (`|`) delimiters.

## Expected Output
```text
MSH|SENDING_APP|2026-01-10|LAB_RESULT
PID|1|DOE^JOHN|1980-05-15|M
OBX|1|NM|Hemoglobin|14.5|g/dL
```
(Notice how the "Object" structure is transformed into a standardized industrial string.)
