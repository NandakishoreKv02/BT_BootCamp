---
title: "Medical Device - Hardware Composition"
type: app_lab
module: oop
unit: unit_4_3_advanced_oop_concepts
lab_number: 2
difficulty: easy
use_case: medical_hardware_modeling
domain: healthcare
order: 2
duration_hours: 0.75
tags:
  topics: ["oop", "advanced-oop", "composition"]
  subtopics:
    - has-a-relationship
    - object-nesting
    - modular-hardware
---

# Lab 2: Hardware Composition

## Overview
Inheritance is powerful, but composition is often preferred for medical hardware where a device "has" many components. In this lab, you will build a `MonitoringDevice` composed of specific `Sensor` objects.

## Use Case: Vital Monitor
A bedside monitor is composed of a `Battery`, a `HeartRateSensor`, and a `BPSensor`. Instead of the monitor *being* a sensor, it *has* them as components.

## Lab Structure
- `Sensor`: Represents a generic hardware component.
- `MonitoringDevice`: The container class that holds several Sensor instances.
