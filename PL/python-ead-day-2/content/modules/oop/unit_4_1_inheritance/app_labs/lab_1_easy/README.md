---
title: "Hospital Staff - Basic Hierarchy"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 1
difficulty: easy
use_case: hospital_staff_management
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["oop", "inheritance", "basics"]
  subtopics:
    - single-inheritance
    - super-keyword
    - attribute-initialization
---

# Lab 1: Hospital Staff - Basic Hierarchy

**Objective**: Create a fundamental class hierarchy for hospital employees using single inheritance.

## Generic Information
**Problem Statement**: A hospital needs to manage different types of staff members. All staff share common attributes (name, ID), but medical staff have specific licensing information.
**Goals**:
- Define a base class `Staff`.
- Create a subclass `MedicalStaff` that inherits from `Staff`.
- Properly initialize parent attributes using `super()`.

## Use Case: Staff Management
We need to represent:
1.  **Staff**: Uses an ID card to enter the building.
2.  **MedicalStaff**: A specialized staff member who also has a medical license number.

## Lab Structure
1.  **Staff Class**: Base attributes.
2.  **MedicalStaff Class**: Inherits and extends.
3.  **Instantiation**: Verify attributes are set correctly.

## Getting Started
In Python, a class inherits by passing the parent class in parentheses: `class Child(Parent):`. inside `__init__`, use `super().__init__(args)` to initialize the parent.
