---
title: "Patient Files - Audit Mixins"
type: app_lab
module: oop
unit: unit_4_3_advanced_oop_concepts
lab_number: 3
difficulty: intermediate
use_case: patient_data_auditing
domain: healthcare
order: 3
duration_hours: 1.0
tags:
  topics: ["oop", "advanced-oop", "mixins"]
  subtopics:
    - multiple-inheritance
    - cross-cutting-concerns
    - logging-mixins
---

# Lab 3: Modular Audit Mixins

## Overview
In high-integrity systems, every data change must be logged. Instead of writing logging code into every class, we use **Mixins**.

## Use Case: Integrity Auditing
Healthcare records must track when they were modified. You will create a `LoggerMixin` that provides a `log_action` method to any class that inherits it.

## Lab Structure
- `LoggerMixin`: Provides logging utilities.
- `AuditableRecord`: A base class for patient data.
- `PatientFile`: Uses multiple inheritance to combine base logic with logging.
