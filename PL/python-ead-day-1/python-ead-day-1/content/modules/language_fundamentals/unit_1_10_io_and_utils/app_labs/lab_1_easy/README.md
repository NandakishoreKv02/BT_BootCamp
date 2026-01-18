---
title: "Interactive Triage Intake"
type: app_lab
module: language_fundamentals
unit: unit_1_10_io_and_utils
lab_number: 1
difficulty: easy
use_case: patient_intake
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["input", "casting"]
  subtopics: ["standard-input"]
---

# Lab 1: Interactive Triage Intake

**Module**: Language Fundamentals  
**Objective**: Build a simple command-line interface (CLI) to collect patient names and ages.  
**Difficulty**: Easy  
**Context**: Healthcare - Emergency Department Front Desk

## Generic Information
**Problem Statement**: You need a script that greets the user, asks for a patient's name and age, and then calculates how many years until they qualify for a senior geriatric screening (at age 65).

## Use Case
**Title**: Senior Screening Calculator  
**Description**: Collect data and perform a projection.

### Rules
- Use `input()` to get the name.
- Use `input()` to get the age.
- Convert age to an `int`.
- Print: `Patient [name] will be 65 in [years] years.`
- If the patient is already 65+, print `Patient [name] is eligible for screening.`

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
