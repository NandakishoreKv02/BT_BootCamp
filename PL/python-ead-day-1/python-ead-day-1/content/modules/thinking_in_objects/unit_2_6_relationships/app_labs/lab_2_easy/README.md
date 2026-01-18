---
title: "The Surgical Kit"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 2
difficulty: easy
use_case: composition-has-a
domain: healthcare
order: 2
duration_hours: 1
tags:
  topics: ["composition", "has-a", "objects-as-attributes"]
---

# Lab 2: The Surgical Kit

**Module**: Thinking in Objects
**Objective**: Implement a **Has-a** (Composition) relationship where one object is responsible for creating and owning its component parts.
**Difficulty**: Easy
**Context**: Sterile Processing

## Problem Statement
A `SurgicalKit` isn't just a container; it is an entity that always contains specific tools. When a new kit is sterilized, it must always be equipped with a `Scalpel` and a `Forceps`.

Your task is to model this relationship where the `SurgicalKit` "owns" these tool objects.

## Requirements
1.  **Tool Classes**:
    - Create a `Scalpel` class with a `sharpness` attribute (100).
2.  **Composition (Has-a)**:
    - Create a `SurgicalKit` class.
    - In its `__init__`, it should create a `Scalpel` object and store it as an attribute (`self.scalpel`).
3.  **Interaction**:
    - Add a method to the kit called `check_readiness()` that returns the sharpness of the contained scalpel.

## Expected Output
```text
Kit sterilized.
Checking scalpel readiness... Sharpness: 100
```
