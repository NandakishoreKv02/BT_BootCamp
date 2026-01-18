---
title: "Hospital Payroll - Salary Calculation"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 3
difficulty: intermediate
use_case: hospital_staff_management
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["oop", "inheritance", "super"]
  subtopics:
    - cumulative-logic
    - method-extension
    - payroll-automation
---

# Lab 3: Hospital Payroll - Salary Calculation

**Objective**: Use `super()` to extend logic in subclasses, building a cumulative logic chain.

## Generic Information
**Problem Statement**: Calculating salary is complex. Every staff member gets a base salary. Medical staff get a hazard pay bonus. Surgeons (a subclass of Medical Staff) get an additional operation bonus.
**Goals**:
- Use `super()` to call the parent's calculation method.
- Add specific bonuses at each hierarchy level without rewriting the base logic.

## Use Case: Payroll
- **Staff**: Base Salary ($50,000).
- **MedicalStaff**: Base + $10,000 Hazard Pay.
- **Surgeon**: (Base + Hazard) + $30,000 Operation Bonus.

## Lab Structure
1.  **Staff**: `calculate_pay()`.
2.  **MedicalStaff (Staff)**: Extends `calculate_pay()`.
3.  **Surgeon (MedicalStaff)**: Extends `calculate_pay()`.
