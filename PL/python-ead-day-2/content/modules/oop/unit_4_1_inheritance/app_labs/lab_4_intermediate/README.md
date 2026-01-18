---
title: "Hospital Admin - Dual Roles"
type: app_lab
module: oop
unit: unit_4_1_inheritance
lab_number: 4
difficulty: intermediate
use_case: hospital_staff_management
domain: healthcare
order: 4
duration_hours: 2.0
tags:
  topics: ["oop", "inheritance", "multiple-inheritance"]
  subtopics:
    - mro-resolution
    - diamond-problem
    - role-integration
---

# Lab 4: Hospital Admin - Dual Roles

**Objective**: Implement multiple inheritance to create a staff member who is both a Doctor and an Administrator, understanding the Method Resolution Order (MRO).

## Generic Information
**Problem Statement**: Some staff members perform dual roles. For example, a "Chief Medical Officer" is both a Doctor (treats patients) and an Administrator (does paperwork).
**Goals**:
- Define `Doctor` and `Administrator` classes.
- Create `ChiefMedicalOfficer` inheriting from both.
- Solve the "Diamond Problem" (or simple conflict) where both parents define the same method.

## Use Case: Dual Roles
- **Doctor**: Method `work()` -> "Treating patient".
- **Administrator**: Method `work()` -> "Doing paperwork".
- **ChiefMedicalOfficer**: Inherits from both. Which `work()` is called?

## Lab Structure
1.  **Doctor Class**: Defines `work()`.
2.  **Administrator Class**: Defines `work()`.
3.  **ChiefMedicalOfficer**: Inherits `(Doctor, Administrator)` vs `(Administrator, Doctor)`.
4.  **MRO Inspection**: Analyze `ChiefMedicalOfficer.mro()`.
