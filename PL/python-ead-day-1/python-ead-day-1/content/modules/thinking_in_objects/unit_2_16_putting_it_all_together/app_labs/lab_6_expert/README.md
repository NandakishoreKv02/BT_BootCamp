---
title: "The Hospital Simulator Capstone"
type: app_lab
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
lab_number: 6
difficulty: expert
use_case: capstone-integration
domain: healthcare
order: 6
duration_hours: 4
tags:
  topics: ["capstone", "full-system", "integration"]
---

# Lab 6: The Hospital Simulator Capstone

**Module**: Thinking in Objects
**Objective**: Build a complete Hospital Management System integrating Patients, Doctors, Departments, and Billing.
**Difficulty**: Expert
**Context**: Hospital Administration

## Problem Statement
You must design a system with the following entities:
1.  **Patient**: Has name, balance, and a list of medical_history.
2.  **Doctor**: Has name and specialty. Can `treat(patient, cost)` which updates patient history and balance.
3.  **Department**: Has a name and a list of doctors. Can `assign_doctor()` returning a doctor of a needed specialty.
4.  **BillingSystem**: Static utility to `generate_invoice(patient)`.

## Requirements
1.  **Integration**:
    - A patient enters the hospital.
    - The department assigns a doctor.
    - The doctor treats the patient (adding a record and cost).
    - The billing system prints the final bill.
2.  **Constraints**:
    - Use Type Hints.
    - Use at least one Static Method.
    - Use proper Encapsulation (e.g., patient balance shouldn't be public, use methods to modify it).

## Expected Output
```text
=== City General Hospital ===
Patient John arrived.
Cardiology assigned Dr. Heart.
Dr. Heart treated John for Angioplasty ($5000).
--- Invoice ---
Patient: John
Total Due: $5000
History: ['Angioplasty']
```
