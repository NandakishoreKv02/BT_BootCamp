---
title: "Interface Standardization - ABCs"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 4
difficulty: intermediate
use_case: medical_device_interface
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["oop", "polymorphism", "abc"]
  subtopics:
    - interface-definition
    - abstract-methods
    - hardware-standardization
---

# Lab 4: Interface Standardization - ABCs

**Objective**: Use Abstract Base Classes to strictly enforce which methods a medical device must implement.

## Generic Information
**Problem Statement**: New developers keep adding devices with inconsistent method names (`start_up`, `boot`, `init`). We need a contract that forces every device to have `connect()` and `get_status()`.
**Goals**:
- Define ABC `MedicalDevice`.
- Enforce `connect()` and `get_status()`.
- Implement `InfusionPump` complying with the interface.

## Use Case: Strict Compliance
- **MedicalDevice**: Abstract. Can't ensure safety if methods are missing.
- **InfusionPump**: Must implement `connect()` (returns passed/failed) and `get_status()` (returns battery %).

## Lab Structure
1.  **ABC Definition**: `MedicalDevice`.
2.  **Concrete Class**: `InfusionPump` inheriting `MedicalDevice`.
3.  **Refusal to Run**: Demonstrate that Python won't instantiate a non-compliant class.
