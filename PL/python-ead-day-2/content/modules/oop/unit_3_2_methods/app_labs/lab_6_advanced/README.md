---
title: "Advanced Workflow Manager"
type: app_lab
module: oop
unit: unit_3_2_methods
lab_number: 6
difficulty: advanced
use_case: workflow_management
domain: healthcare
order: 6
duration_hours: 4
tags:
  topics: ["oop", "methods"]
  subtopics:
    - return-values
    - side-effects
    - coordination
---

# Lab 6: Advanced Workflow Manager

**Module**: Object-Oriented Programming - Part 1
**Objective**: Differentiate and coordinate side effects (state changes) and return values (queries).
**Difficulty**: Advanced
**Context**: Pharmacy Management

## Generic Information
**Problem Statement**: In a hospital pharmacy, "Dispensing" a medication is a complex action. It must change the inventory status (side effect) and inform the nurse if the operation was successful (return value).
**Goals**:
- Implement methods that perform complex state changes.
- Return status codes or result messages.
- Chain methods together to execute a workflow.

## Use Case
**Title**: Dispense Medication
**Description**: A patient is prescribed a drug. The method should update the patient's record and return a success message or an error if the drug is already active.

### Rules
- A patient cannot have two active prescriptions of the same drug.
- The system must track usage history.

### Test Cases
- Case 1: First prescription succeeds.
- Case 2: Duplicate prescription fails with a clear error message.

### Success Criteria
- Patient state is correctly updated.
- Return values accurately reflect the outcome.

## Overview
This lab combines everything learned about instance methods to build complex, reliable transaction-like operations in code.

---
