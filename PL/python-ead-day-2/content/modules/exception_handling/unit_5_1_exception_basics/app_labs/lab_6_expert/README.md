---
title: "Configuration Loader - Robust System Integration"
type: app_lab
module: exception_handling
unit: unit_5_1_exception_basics
lab_number: 6
difficulty: expert
use_case: system_config
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["exceptions", "IOError", "JSONDecodeError"]
  subtopics:
    - file-handling
    - json-parsing
    - default-fallbacks
---

# Lab 6: Configuration Loader - Robust System Integration

**Objective**: Create a fault-tolerant configuration loader that handles missing files, permission errors, and corrupted JSON without crashing the application.

## Generic Information
**Problem Statement**: System configurations are read at startup. Steps: 1. Open file. 2. Read content. 3. Parse JSON. 4. Validate keys.
Any of these can fail.
- File missing? Use default config.
- File corrupted? Log error and use default.
- Permission denied? Log critical error and exit (or use default).
This lab requires handling `FileNotFoundError`, `PermissionError`, and `json.JSONDecodeError`.

## Use Case: Robust System Integration
The "MriScanner" boots up. If `config.json` is corrupted, it shouldn't crash. It should load in "Safe Mode" (defaults).

## Lab Structure
1.  **File Reader**: Safely opening the file.
2.  **Parser**: Safely parsing JSON.
3.  **Fallback Mechanism**: Returning defaults when things fail.

## Getting Started
You will need to import `json`. Notice that `FileNotFoundError` and `PermissionError` are both `OSError` subclasses, but we might want to handle them differently (e.g., Missing file = Warning, Permission = Error).
