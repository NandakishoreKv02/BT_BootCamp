---
title: "Medical Reports - Factory Pattern"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 2
difficulty: easy
use_case: multi_format_reporting
domain: healthcare
order: 2
duration_hours: 0.75
tags:
  topics: ["oop", "design-patterns", "factory"]
  subtopics:
    - object-creation
    - partial-abstraction
    - report-formats
---

# Lab 2: Multi-Format Report Factory

## Overview
Clinicians need different types of reports. A doctor might want a detailed PDF, while a data analyst might want a CSV. In this lab, you'll use a **Factory** to create these objects dynamically.

## Use Case: Discharge Summaries
You will build a `ReportFactory` that creates either `PDFReport` or `CSVReport` objects based on a user's selection.

## Lab Structure
- `MedicalReport`: Base abstract class for all reports.
- `PDFReport` & `CSVReport`: Implementation classes.
- `ReportFactory`: The central creation point.
