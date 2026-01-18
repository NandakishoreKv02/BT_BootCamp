---
title: "HL7 Field Extractor"
type: app_lab
module: language_fundamentals
unit: unit_1_4_variables_and_data_types
lab_number: 5
difficulty: advanced
use_case: interoperability
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["string-manipulation", "immutability"]
  subtopics: ["indexing", "escaping"]
---

# Lab 5: HL7 Field Extractor

**Module**: Language Fundamentals  
**Objective**: Parse specific fields from an HL7 string and prove understanding of string immutability.  
**Difficulty**: Advanced  
**Context**: Healthcare - System Interoperability

## Generic Information
**Problem Statement**: HL7 messages use pipe `|` delimiters. You need to extract the Patient Name (Field 5 in PID) and Date of Birth (Field 7 in PID). Also, perform a "masking" operation (replacing name with *) and demonstrate that this creates a NEW string, keeping the original intact.

**Goals**:
- String indexing and slicing.
- `split()` method.
- Concept: modifying a string = creating a new one.

## Use Case
**Title**: PID Segment Parser
**Description**: `PID|1||12345^^^MRN||DOE^JOHN||19800101|M`

### Rules
- `extract_pid_fields(pid_segment)` -> returns Dict `{'name': 'DOE^JOHN', 'dob': '19800101'}`.
- `mask_patient_name(pid_segment)` -> returns NEW string where 'DOE^JOHN' is replaced by '***'. Use `replace()` or slicing logic.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
