---
title: "Nurse Alerts - Observer Pattern"
type: app_lab
module: oop
unit: unit_4_4_design_patterns
lab_number: 3
difficulty: intermediate
use_case: real_time_notifications
domain: healthcare
order: 3
duration_hours: 1.0
tags:
  topics: ["oop", "design-patterns", "observer"]
  subtopics:
    - subject-observer
    - event-broadcasting
    - dynamic-subscribers
---

# Lab 3: Nurse Station Alerting System

## Overview
When a patient's heart rate spikes, several systems need to know: the Nurse's dashboard, the Physician's pager, and the system log. Instead of the monitor knowing about all these targets, it simply "notifies" its observers.

## Use Case: Vital Sign Alerts
You will build a `VitalMonitor` (the Subject) that broadcasts alerts to multiple registered observers (Station, Pager, Logger).

## Lab Structure
- `Subject` Base: Manages the list of observers.
- `VitalMonitor`: Concrete subject that detects breaches.
- `Observer` Interface: Abstract base for all listening endpoints.
