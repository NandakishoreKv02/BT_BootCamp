---
title: "HL7 Message Parser Library"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 6
difficulty: expert
use_case: interoperability
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["string-manipulation", "modules", "documentation"]
  subtopics: ["parsing", "hl7", "library-development"]
---

# Lab 6: HL7 Message Parser Library

**Module**: Language Fundamentals  
**Objective**: Develop a professional-grade "library" module for parsing HL7 medical messages, featuring rigorous documentation and structure.  
**Difficulty**: Expert  
**Context**: Healthcare - System Interoperability

## Generic Information
**Problem Statement**: HL7 (Health Level 7) is the standard for exchanging medical data. You need to build a reusable Python module that parses raw HL7 strings into usable dictionaries. As a core library, it must be impeccably structured, documented (PEP 257), and safely importable.

**Goals**:
- Create a reusable library module
- Parse standard pipe-delimited strings
- Provide comprehensive docstrings describing the data format
- Organize code into `parse` and `create` functions

## Use Case
**Title**: HL7 V2.x Parser  
**Description**: Parse segments like `PID` (Patient ID) and `OBX` (Observation/Result).

### Segment Structure
`PID|1|123456^^^MRN|...|DOE^JOHN`
- Pipe `|` separates fields.
- Caret `^` separates sub-components.

### Rules
1. **Modules**: The file must act as a standalone library.
2. **Function**: `parse_message(hl7_string)` returns a list of dictionaries.
3. **Function**: `get_patient_name(parsed_message)` extracts the name from PID segment.
4. **Documentation**: Every function needs a full Google-style or NumPy-style docstring.

## Overview
This lab simulates building a piece of core infrastructure logic.

## Learning Goals
- Designing high-quality modules
- Professional documentation standards
- Complex string manipulation logic

## How to Use This Lab
1. Read `tasks.md`
2. Edit `starter_code.py`
3. Run `tests.py`
