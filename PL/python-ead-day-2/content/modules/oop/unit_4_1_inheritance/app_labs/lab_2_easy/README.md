---
title: "Hospital Security - Access Control"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 2
difficulty: easy
use_case: hospital_staff_management
domain: healthcare
order: 2
duration_hours: 1.0
tags:
  topics: ["oop", "inheritance", "overriding"]
  subtopics:
    - method-overriding
    - security-levels
    - access-management
---

# Lab 2: Hospital Security - Access Control

**Objective**: Implement method overriding to enforce different security access levels.

## Generic Information
**Problem Statement**: While all staff can enter the building, only some (Medical Staff) should have access to patient records.
**Goals**:
- Define a method `access_records()` in the base class.
- Override this method in the subclass to provide different behavior.

## Use Case: Record Access
- **Generic Staff**: When attempting to access records, denied.
- **Medical Staff**: When attempting to access records, granted.

## Lab Structure
1.  **Staff Class**: Default behavior (Access Denied).
2.  **MedicalStaff Class**: Overridden behavior (Access Granted).
