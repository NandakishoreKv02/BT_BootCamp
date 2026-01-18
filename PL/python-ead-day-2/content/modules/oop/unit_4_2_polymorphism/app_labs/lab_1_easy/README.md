---
title: "Universal Reader - Duck Typing"
type: app_lab
module: oop
unit: unit_4_2_polymorphism
lab_number: 1
difficulty: easy
use_case: medical_device_interface
domain: healthcare
order: 1
duration_hours: 1.0
tags:
  topics: ["oop", "polymorphism", "duck-typing"]
  subtopics:
    - dynamic-typing
    - interface-substitution
    - device-reading
---

# Lab 1: Universal Reader - Duck Typing

**Objective**: Implement a function that reads data from different medical devices without checking their specific class types.

## Generic Information
**Problem Statement**: Hospitals use Thermometers and Oximeters from different manufacturers. They don't share a code base, but they both have a method to get their current reading. We need a way to read from both using one function.
**Goals**:
- Create two independent classes: `Thermometer` and `Oximeter`.
- Implement a `read()` method in both.
- Create a `collect_data()` function that works with any object having a `read()` method.

## Use Case: Device Interface
- **Thermometer**: `read()` returns a temperature string (e.g., "98.6 F").
- **Oximeter**: `read()` returns an oxygen level string (e.g., "98%").
- **Collector**: Iterates through a mix of devices and prints readings.

## Lab Structure
1.  **Device Classes**: Simple classes with no inheritance relationship.
2.  **Polymorphic Function**: A function accepting an object and calling `.read()`.
3.  **Verification**: Passing both types to the function.

## Getting Started
Remember the Duck Typing philosophy: "If it has a `read()` method, we can read from it." You do not need to use `isinstance`.
