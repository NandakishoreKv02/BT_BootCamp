---
title: "The BCE Controller Pattern"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 5
difficulty: advanced
use_case: enterprise-architecture
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["bce", "controller-pattern", "separation-of-concerns"]
---

# Lab 5: The BCE Controller Pattern

**Module**: Thinking in Objects
**Objective**: Implement a complete architectural flow using the **Boundary-Control-Entity** pattern. Master how a "Control" class acts as the brain that coordinates data flow.
**Difficulty**: Advanced
**Context**: Admission & Registration System

## Problem Statement
In a complex system, the User Interface (Boundary) should never talk directly to the Database (Entity). Instead, they should go through a **Controller**. This allows you to change the UI (switching from CLI to a Web App) without touching your business logic or your data structure.

You will build a `RegistrationController` that validates a patient before adding them to the hospital's central list.

## Requirements
1.  **Entity**: `Patient` (Simple name/MRN data).
2.  **Boundary**: `RegistrationUI` (Contains `input` prompts and `print` statements).
3.  **Control**: `RegistrationController` (Contains `validate()` and `register()` methods).
4.  **Flow**:
    - The UI collects data.
    - The UI sends data to the Controller.
    - The Controller validates (e.g., MRN must be 4 digits).
    - If valid, the Controller creates an Entity and stores it.

## Expected Output
```text
Collecting data for John...
CONTROLLER: Validating MRN 1001...
SUCCESS: Patient John registered.
```
