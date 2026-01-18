---
title: "Access Control - Exception Attributes"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 2
difficulty: easy
use_case: data_rich_errors
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["exceptions", "attributes", "__init__"]
  subtopics:
    - structured-errors
    - error-codes
---

# Lab 2: Access Control - Exception Attributes

**Objective**: Create a `SecurityError` that carries the `user_id` and the `resource_id` that caused the violation, allowing for structured logging.

## Generic Information
**Problem Statement**: "Access Denied" is not enough info. The security logs need to know WHO tried to access WHAT.
**Goals**:
- Define `class SecurityError(Exception)`.
- Override `__init__` to accept `user` and `resource`.
- Store them as attributes.

## Use Case: Data Rich Errors
The "AuditLog" catches exceptions and writes: "User Bob tried to access Record 999".

## Lab Structure
1.  **Rich Exception**: Custom `__init__`.
2.  **Guard Function**: Check permissions and raise.
3.  **Logger**: Inspecting `e.user` and `e.resource`.

## Getting Started
Don't forget `super().__init__(message)` if you want a default string message.
