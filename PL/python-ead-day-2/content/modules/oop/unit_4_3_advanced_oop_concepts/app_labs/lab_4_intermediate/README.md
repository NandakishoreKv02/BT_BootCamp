---
title: "Prescription History - Advanced Dataclasses"
type: app_lab
module: oop
unit: unit_4_3_advanced_oop_concepts
lab_number: 4
difficulty: intermediate
use_case: prescription_management
domain: healthcare
order: 4
duration_hours: 1.0
tags:
  topics: ["oop", "advanced-oop", "dataclasses"]
  subtopics:
    - mutable-defaults
    - frozen-dataclasses
    - post-init-validation
---

# Lab 4: Advanced Dataclasses

## Overview
Standard dataclasses fail when dealing with mutable defaults (like lists) because Python shares the list across all instances. In this lab, you will learn to use `field(default_factory=list)` correctly.

## Use Case: Prescription History
A `PrescriptionRecord` contains a list of medications. This list must be unique for every instance. Additionally, some records must be `frozen` to prevent tempering.

## Lab Structure
- `Medication`: Simple dataclass.
- `PrescriptionRecord`: Advanced dataclass using `default_factory`.
- `ArchiveRecord`: A `frozen` dataclass for historical data.
