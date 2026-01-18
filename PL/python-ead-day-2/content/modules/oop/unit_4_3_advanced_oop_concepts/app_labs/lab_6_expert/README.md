---
title: "Monitor Plugins - Metaclass Registry"
type: app_lab
module: oop
unit: unit_4_3_advanced_oop_concepts
lab_number: 6
difficulty: expert
use_case: automated_plugin_registration
domain: healthcare
order: 6
duration_hours: 1.5
tags:
  topics: ["oop", "advanced-oop", "metaclasses"]
  subtopics:
    - class-interception
    - metaclass-new
    - automatic-registry
---

# Lab 6: Advanced Registry with Metaclasses

## Overview
As the OmniCare system grows, developers will add new specialized `Monitor` classes (e.g., `VentilatorMonitor`, `InfusionMonitor`). We shouldn't have to manually add these to a list. A **Metaclass** can handle this automatically the moment a class is defined.

## Use Case: Dynamic Plugin System
You will build a `MonitorRegistry` metaclass that:
1.  Stores a list of all subclasses created.
2.  Ensures every subclass has a `MONITOR_ID` attribute.
3.  Rejects any class that doesn't follow the naming convention.

## Lab Structure
- `MonitorRegistry`: The metaclass (of `type`).
- `BaseMonitor`: The parent class that uses the metaclass.
- `ConcreteMonitors`: Child classes that are automatically tracked.
