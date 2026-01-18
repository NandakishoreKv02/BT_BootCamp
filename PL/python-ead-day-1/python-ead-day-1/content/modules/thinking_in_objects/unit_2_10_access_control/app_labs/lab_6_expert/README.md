---
title: "The Self-Calibrating Surgical Assist"
type: app_lab
module: thinking_in_objects
unit: unit_2_10_access_control
lab_number: 6
difficulty: expert
use_case: complex-encapsulation-workflow
domain: healthcare
order: 6
duration_hours: 3
tags:
  topics: ["private-methods", "encapsulation", "logic-abstraction"]
---

# Lab 6: The Self-Calibrating Surgical Assist

**Module**: Thinking in Objects
**Objective**: Use **Private Methods** (abstraction) and **Properties** (validation) to manage a complex, multi-stage business process within a single class.
**Difficulty**: Expert
**Context**: Robotics Engineering

## Problem Statement
A `SurgicalRobot` must be extremely safe.
1.  **State Management**: It has an `arm_extension` (0 to 100 cm).
2.  **Encapsulation**: External users should NOT manually set the arm extension. They should call a public method `calibrate_and_deploy()`.
3.  **Process Abstraction**: The calibration involves several internal checks (e.g., `__check_power`, `__verify_position`). These must be **Private**—the user doesn't need to know they exist, they just want the robot to move.

## Requirements
1.  **Strict Privacy**:
    - All check methods (power, position, sensors) must use `__`.
    - Internal state `__extension` must be private.
2.  **Public Interface**:
    - `@property` `is_ready` (boolean).
    - `deploy(self, length)` method.
3.  **Encapsulated Logic**:
    - The `deploy` method should call the private checks internally. If any check fails, the move is blocked.

## Expected Output
```text
Initiating Deployment: 50cm
  [LOG] Power Check... OK
  [LOG] Position Verify... OK
Robot arm extended to 50cm.
```
