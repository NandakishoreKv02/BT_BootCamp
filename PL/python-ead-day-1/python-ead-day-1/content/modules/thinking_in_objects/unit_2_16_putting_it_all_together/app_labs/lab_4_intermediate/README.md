---
title: "The Patient Portal"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 4
difficulty: intermediate
use_case: srp-security
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["srp", "encapsulation", "properties"]
---

# Lab 4: The Patient Portal

**Module**: Thinking in Objects
**Objective**: Build a secure `PatientAccount` class that uses proper encapsulation and adheres to SRP by delegating logging to a separate `AuditLog` class.
**Difficulty**: Intermediate
**Context**: Online Records

## Problem Statement
We need a class to manage patient logins.
1.  **Security**: The password must be private.
2.  **Audit**: Every login attempt (success or fail) must be logged.
3.  **SRP**: The `PatientAccount` shouldn't know *how* to write to a log file; it should use an `AuditLog` object.

## Requirements
1.  **Class `AuditLog`**:
    - Method `log_entry(msg)`: Prints/Stores "LOG: {msg}".
2.  **Class `PatientAccount`**:
    - Init with `username` and `password`.
    - Method `login(pw, log_system)`: Checks password. Calls `log_system.log_entry` with the result.

## Expected Output
```text
LOG: Login success for user alice
LOG: Login failed for user alice
```
