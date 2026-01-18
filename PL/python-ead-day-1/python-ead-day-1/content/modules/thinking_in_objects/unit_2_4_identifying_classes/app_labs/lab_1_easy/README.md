---
title: "The Triage Noun-Verb Mapper"
type: app_lab
module: thinking_in_objects
unit: unit_2_4_identifying_classes
lab_number: 1
difficulty: easy
use_case: analysis-to-code
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["analysis", "modeling", "class-design"]
---

# Lab 1: The Triage Noun-Verb Mapper

**Module**: Thinking in Objects
**Objective**: Translate a written clinical requirement into a functional set of classes following the Noun-Verb analysis technique.
**Difficulty**: Easy
**Context**: Emergency Room Triage

## Problem Statement
A Hospital Director provides the following requirement:
*"A **TriageNurse** must be able to create a **PatientRecord**. The nurse should then be able to **calculate** the **UrgencyScore** based on the patient's symptoms."*

Your task is to implement the two main "Nouns" identified as classes and the "Verb" as a method.

## Requirements
1.  **Modeling**:
    - Identify the Nouns: `TriageNurse`, `PatientRecord`.
    - Identify the Verbs: `calculate_urgency`.
2.  **Implementation**:
    - Create a `PatientRecord` class to store name and symptoms.
    - Create a `TriageNurse` class.
    - Add a method to `TriageNurse` that takes a `PatientRecord` and returns an urgency score (1-5).

## Expected Output
```text
Nurse Nightingale is assessing Patient John...
Urgency Score Calculated: 4
```
