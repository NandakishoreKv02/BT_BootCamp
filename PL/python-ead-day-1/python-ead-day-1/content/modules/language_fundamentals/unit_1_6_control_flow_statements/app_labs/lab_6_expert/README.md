---
title: "Automated Billing Generator"
type: app_lab
module: language_fundamentals
unit: unit_1_6_control_flow_statements
lab_number: 6
difficulty: expert
use_case: financial_management
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["nested-logic", "calculations"]
  subtopics: ["billing", "parsing"]
---

# Lab 6: Automated Billing Generator

**Module**: Language Fundamentals  
**Objective**: Parse nested patient procedure data and calculate total costs applying various discounts and surcharge rules based on control flow logic.  
**Difficulty**: Expert  
**Context**: Healthcare - Revenue Cycle Management (RCM)

## Generic Information
**Problem Statement**: Hospital billing is complex. A patient might have multiple procedures. Each procedure has a base cost, but rules apply:
- If procedure is "Emergency", add 20% surcharge.
- If total bill exceeds $500, apply a 10% discount on the **entire** total.
- Skip "Cancelled" procedures.

## Use Case
**Title**: Multi-Scenario Billing Engine  
**Description**: Calculate final bill for a patient.

### Rules
- `calculate_bill(procedures)`
- Input: `[{"service": "X", "cost": 100, "is_emergency": True, "status": "Done"}, ...]`
- Logic:
  - Initialize `total = 0`.
  - Loop through procedures.
  - If `status == "Cancelled"`, skip.
  - Add `cost` to total.
  - If `is_emergency`, add `cost * 0.2` to total.
  - After loop, if `total > 500`, multiply `total` by `0.9`.
- Return `total` rounded to 2 decimal places.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
