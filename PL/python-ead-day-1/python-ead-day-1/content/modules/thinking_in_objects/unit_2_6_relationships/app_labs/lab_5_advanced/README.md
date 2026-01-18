---
title: "The Robotic Surgery System"
type: app_lab
module: thinking_in_objects
unit: unit_2_6_relationships
lab_number: 5
difficulty: advanced
use_case: complex-interaction
domain: healthcare
order: 5
duration_hours: 2
tags:
  topics: ["composition", "dependency", "modeling"]
---

# Lab 5: The Robotic Surgery System

**Module**: Thinking in Objects
**Objective**: Build a complex "System of Systems" where an object has internal components (**Composition**) but must also interact with external resources (**Dependency**).
**Difficulty**: Advanced
**Context**: Surgical Robotics

## Problem Statement
A `SurgicalRobot` is a complex machine used for precision surgery. 
1.  **Composition**: Every robot *has* a built-in `Camera` and a `MechanicalArm`. These are permanent parts of the robot.
2.  **Dependency**: To perform an actual procedure, the robot **uses** a `PowerSource` (external) and **uses** a `TargetOrgan` (passed as an argument) to perform the incision.

Your task is to model this multi-layered interaction, ensuring a clear distinction between what the robot *owns* and what it *calls*.

## Requirements
1.  **Modeling**:
    - Build `Camera` and `MechanicalArm` classes.
    - Build `PowerSource` and `Organ` classes.
    - Build `SurgicalRobot` class.
2.  **Implementation**:
    - The robot should create its Camera and Arm in `__init__`.
    - It should have a method `perform_surgery(self, power, organ)` which uses the external objects to print the result.
3.  **Simulation**:
    - Ensure the arm "sharpness" or "strength" is accessed during the method call.

## Expected Output
```text
ROBOT STATUS: Camera Online. Arm Active.
POWER STATUS: Source Connected.
INCISION: Incising Appendix with 100% precision.
```
