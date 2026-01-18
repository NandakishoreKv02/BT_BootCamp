---
title: "Multi-Patient Management System"
type: app_lab
module: language_fundamentals
unit: unit_1_12_hands_on_labs
lab_number: 5
difficulty: advanced
use_case: patient_management
domain: healthcare
order: 5
duration_hours: 4
tags:
  topics: ["integration", "crud-operations", "data-validation"]
  subtopics: ["multi-entity-management"]
---

# Lab 5: Multi-Patient Management System

**Objective**: Build a comprehensive patient management system with CRUD operations, search, filtering, and data validation.

## Requirements
- Store multiple patients (list of dicts)
- Add, update, delete, search patients
- Filter by age range, diagnosis
- Validate data (age > 0, required fields)
- Display formatted patient list
- Export to file

### Core Functions
- `add_patient(patients, mrn, name, age, diagnosis)`
- `find_patient_by_mrn(patients, mrn)`
- `update_patient(patients, mrn, **kwargs)`
- `delete_patient(patients, mrn)`
- `filter_by_age_range(patients, min_age, max_age)`
- `filter_by_diagnosis(patients, diagnosis)`
- `display_patients(patients)`
- `export_to_file(patients, filename)`
