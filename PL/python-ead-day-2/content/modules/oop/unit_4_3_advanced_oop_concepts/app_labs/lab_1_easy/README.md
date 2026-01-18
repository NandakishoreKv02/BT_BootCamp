---
title: "Patient Vitals - Dataclasses"
type: app_lab
module: oop
unit: unit_4_3_advanced_oop_concepts
lab_number: 1
difficulty: easy
use_case: patient_vitals_tracking
domain: healthcare
order: 1
duration_hours: 0.75
tags:
  topics: ["oop", "advanced-oop", "dataclasses"]
  subtopics:
    - dataclass-decorator
    - type-hints
    - auto-methods
---

# Lab 1: Patient Vitals via Dataclasses

## Overview
In this lab, you will move away from writing manual `__init__` and `__repr__` methods for data-holding classes. You will implement the `VitalsRecord` using Python's `@dataclass` decorator.

## Use Case: Telemetry Data Points
OmniCare needs a way to store snapshots of patient vitals (Heart Rate, Temperature, Blood Pressure) as they arrive from sensors. These objects are primarily data containers.

## Lab Structure
- `VitalsRecord`: A dataclass storing heart rate, temperature, and blood pressure.
- `PatientHeader`: A dataclass storing basic identifying information.
