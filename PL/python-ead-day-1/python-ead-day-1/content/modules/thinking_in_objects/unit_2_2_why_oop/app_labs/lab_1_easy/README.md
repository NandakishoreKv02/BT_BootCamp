---
title: "Hospital Config Manager"
type: app_lab
module: thinking_in_objects
unit: unit_2_2_why_oop
lab_number: 1
difficulty: easy
use_case: modularity
domain: healthcare
order: 1
duration_hours: 1
tags:
  topics: ["modularity", "dictionaries", "configuration"]
---

# Lab 1: Hospital Config Manager

**Module**: Thinking in Objects
**Objective**: Demonstrate **Modularity** by creating a standalone `Config` component that manages system settings, separating it from the main application logic.
**Difficulty**: Easy
**Context**: Clinical System Settings

## Problem Statement
A hospital application has many settings: `hospital_name`, `api_endpoint`, and `encryption_enabled`. Currently, these are scattered as global variables throughout the code. If we want to change from "Production" mode to "Test" mode, we have to manually hunt down and change 10 different lines.

Your task is to encapsulate these settings into a single `Config` object (dictionary), ensuring that the application remains modular and easy to reconfigure.

## Requirements
1.  **Encapsulation**: Create a `make_config(env)` function that returns a dictionary of settings based on the environment ("test" or "prod").
2.  **Modularity**: Define functions like `get_connection_info(config)` that depend strictly on the config object, not on global variables.
3.  **Independence**: Ensure that changing the values in one config object doesn't affect another, proving that state is correctly encapsulated.

## Expected Output
```text
Connecting to https://api.hospital.com for hospital City General (Secure: True)
Connecting to http://localhost:8080 for hospital Mock Hospital (Secure: False)
```
(Notice how the application behavior changes based on which Object is passed to the function.)
