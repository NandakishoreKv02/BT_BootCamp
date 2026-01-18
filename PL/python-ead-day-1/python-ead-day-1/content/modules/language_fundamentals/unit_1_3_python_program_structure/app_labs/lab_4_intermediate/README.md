---
title: "Importable Logger"
type: app_lab
module: language_fundamentals
unit: unit_1_3_python_program_structure
lab_number: 4
difficulty: intermediate
use_case: system_logging
domain: healthcare
order: 4
duration_hours: 1
tags:
  topics: ["modules", "imports", "main-guard"]
  subtopics: ["library-design", "avoiding-side-effects"]
---

# Lab 4: Importable Logger

**Module**: Language Fundamentals  
**Objective**: Create a logging utility module that can be safely imported without side effects.  
**Difficulty**: Intermediate  
**Context**: Healthcare - System Auditing

## Generic Information
**Problem Statement**: In large hospital systems, utility scripts (like loggers) are often imported by many other modules. A common mistake is putting executable code (like `print("Logger initialized")`) at the top level, which spams the console every time the module is imported.

**Goals**:
- Implement a reusable `log_message` function
- Use the `__main__` guard to separate library code from execution code
- Ensure zero side effects on import

## Use Case
**Title**: Audit Logger  
**Description**: A simple logger that formats messages with timestamps.

### Rules
- Function `log_message(level, msg)` returns "[TIMESTAMP] [LEVEL] msg".
- When run directly: Prints a demo "Logger Demo Started".
- When imported: Prints NOTHING.

### Test Cases
- Run `python starter_code.py` -> Output includes "Logger Demo Started"
- Run `python -c "import starter_code"` -> Output is EMPTY

## Overview
This lab drills the "Main Guard" concept, essential for modular Python programming.

## Learning Goals
- Understand "Side Effects on Import"
- Master `if __name__ == "__main__":`

## How to Use This Lab
1. Read `tasks.md`
2. Edit `starter_code.py`
3. Run `tests.py`
