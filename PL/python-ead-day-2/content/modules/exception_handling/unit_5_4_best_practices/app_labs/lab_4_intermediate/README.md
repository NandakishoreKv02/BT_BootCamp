---
title: "The Polite Secretary - User Error Messages"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 4
difficulty: intermediate
use_case: patient_ux
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["exceptions", "ux", "messages"]
  subtopics:
    - security
    - friendly-errors
---

# Lab 4: The Polite Secretary - User Error Messages

**Objective**: Implement a handler that logs technical details for developers but returns a polite, helpful, and non-sensitive message to the end-user.

## Generic Information
**Problem Statement**: Users don't care about `PermissionError: [Errno 13] Access denied: 'C:\\Users\\...'`. In fact, showing this is a security risk. You should log the technical detail but tell the user something they can act on.
**Goals**:
- Handle a `PermissionError`.
- Log the technical file path to a hidden list.
- Return a "User-Friendly" message string.

## Use Case: Patient UX
A patient tries to download their medical report. If the file server disk is full or has a permission bug, the patient shouldn't see "DiskFullError". They should see "Sorry, we are having trouble retrieving your report. Please contact support."

## Lab Structure
1.  **Operation**: Attempting to read a file.
2.  **Dual Response**: Logging vs Returning.
3.  **Security Check**: Ensuring NO paths are in the return message.

## Getting Started
Internal: "Technical detail for us."
External: "Polite message for them."
