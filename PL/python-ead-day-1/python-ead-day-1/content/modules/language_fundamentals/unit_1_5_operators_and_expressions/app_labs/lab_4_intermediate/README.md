---
title: "Secure Access Validator"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 4
difficulty: intermediate
use_case: security
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["membership", "identity"]
  subtopics: ["authorization", "null-checks"]
---

# Lab 4: Secure Access Validator

**Module**: Language Fundamentals  
**Objective**: Validate user access by checking if a role exists in an allowed list and ensuring a user object is not null.  
**Difficulty**: Intermediate  
**Context**: Healthcare - System Access

## Generic Information
**Problem Statement**: Healthcare software must strictly control who sees patient data. You need to write a validator that checks two things:
1. Is the current user object initialized? (Not `None`)
2. Does the user have a role that is in the "Approved Roles" list?

## Use Case
**Title**: Role Membership Check  
**Description**: Validate access based on User Identity and Role.

### Rules
- `is_access_authorized(user_obj, user_role)`
- `APPROVED_ROLES = ["Doctor", "Nurse", "Admin"]`
- Return `True` ONLY if `user_obj` is NOT `None` AND `user_role` is in the `APPROVED_ROLES` list.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
