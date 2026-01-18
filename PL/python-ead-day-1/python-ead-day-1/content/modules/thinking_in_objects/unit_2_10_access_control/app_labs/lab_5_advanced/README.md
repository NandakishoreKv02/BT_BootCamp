---
title: "The Immutable Patient Key"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 5
difficulty: advanced
use_case: read-only-encapsulation
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["read-only-property", "private-members", "data-integrity"]
---

# Lab 5: The Immutable Patient Key

**Module**: Thinking in Objects
**Objective**: Combine private attributes with properties to create an "Identity Lock" for clinical records.
**Difficulty**: Advanced
**Context**: EHR Identity Management

## Problem Statement
In an EHR system, once a patient is registered, their `mrn` (Medical Record Number) must NEVER change. Their name can change (e.g., marriage), but the MRN is the immutable anchor of their history.

Your task is to implement a `ClinicalRecord` class where the MRN is strictly read-only and uses name mangling to prevent even accidental protected access.

## Requirements
1.  **Strict Private Storage**:
    - Use double underscore `__mrn` to store the record number.
2.  **Public Read-Only Interface**:
    - Build a `@property` named `mrn` to return the value.
    - DO NOT provide a setter for `mrn`.
3.  **Mutable Interface**:
    - Provide a property for `name` that HAS a setter (allowing legitimate name changes).

## Expected Output
```text
Patient: John Doe [MRN: 12345]
Changing name to John Smith...
Updated Patient: John Smith [MRN: 12345]
(Attempting to change MRN...)
Error: can't set attribute
```
