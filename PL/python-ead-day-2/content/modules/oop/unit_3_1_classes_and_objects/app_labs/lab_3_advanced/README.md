---
title: "Hospital Registry System"
type: app_lab
module: oop
unit: unit_3_1_classes_and_objects
lab_number: 3
difficulty: advanced
use_case: hospital_registry_management
domain: healthcare
order: 3
duration_hours: 4
tags:
  topics: ["oop", "class-variables"]
  subtopics:
    - class-variables
    - managing-instances
    - coordination
    - identity-vs-equality
---

# Lab 3: Hospital Registry System

**Module**: Object-Oriented Programming - Part 1
**Objective**: Master shared state (class variables) and interaction between different objects.
**Difficulty**: Advanced
**Context**: Hospital Facility Management

## Generic Information
**Problem Statement**: As the facility grows, we need to manage shared data (like the Hospital Name) and maintain a central registry of all patients. Storing the hospital name in every single patient object is redundant and makes updates difficult. Moreover, we need a way to look up specific patient objects from a collection.
**Goals**:
- Use class variables to store shared facility information.
- Use a registry class to manage a collection of Patient objects.
- Implement logic to search for objects by identity and attributes.
**Data Elements**:
- `clinic_name`: A class-variable shared by all patients.
- `patients`: A list containing Patient objects.

## Use Case
**Title**: Manage Hospital Registry
**Description**: The hospital administrator needs a central system to view all registered patients and update shared hospital details globally.

### Rules
- All patients must share the same `clinic_name`.
- If the clinic name is updated, every patient object must reflect this change immediately.

### Test Cases
- Case 1: Change the clinic name in the class and verify all instances show the new name.
- Case 2: Use the `registry` to find a specific patient by their ID.
- Case 3: Compare two patient objects with the same data to see if they are the same instance.

### Success Criteria
- Global hospital name updates work as expected.
- Registry correctly stores and retrieves objects.
- Correct distinction between `is` and `==`.

## Overview
This advanced lab challenges you to think architecturally. You will separate the concerns of "What is a Patient?" from "How do we manage the collection of all Patients?".

## Learning Goals
- Implement and update class-level variables.
- Practice the "Controller" pattern by creating a registry class.
- Manage references between objects.
- Deepen understanding of object identity.

## The Scenario
The clinical management software is scaling up. The system now needs to identify which specific hospital a patient belongs to and provide administrators with a master list.

## What You'll Build
You will create a `HospitalRegistry` class that acts as a container and manager for the `Patient` instances created in previous labs.

## How to Use This Lab
1. **Analyze** the architecture requirements in `tasks.md`.
2. **Implement** the coordination logic in `starter_code.py`.
3. **Run** `tests.py` to check system integrity.

## Task Summary
- Task 1: Incorporate a Class Variable.
- Task 2: Create the HospitalRegistry Class.
- Task 3: Implement search functionality.
- Task 4: Global Updates.

## Time Estimate
- Understanding requirements: 20 minutes
- Implementation: 3 - 4 hours
- Testing & refinement: 30 minutes
- **Total**: ~5 hours
---
