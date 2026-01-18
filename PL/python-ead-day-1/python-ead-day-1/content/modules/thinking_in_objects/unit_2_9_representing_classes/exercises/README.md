# Unit 2.9: Representing Classes – Exercises

## Overview
These exercises focus on the technical implementation details of Python classes. You will practice PEP 8 compliance, implement robust constructors, and master the use of `self` for instance-level state management.

## Instructions
1.  Open `unit_2_9_representing_exercises.py`.
2.  Complete the 4 syntax and standards challenges.
3.  Run the file to verify your work:
    ```bash
    python unit_2_9_representing_exercises.py
    ```

## Exercise List

### 1. The PEP 8 Auditor
**Concepts**: Naming Conventions  
**Task**: Rename a messy clinical class and its methods to strictly follow PEP 8 standards (PascalCase for classes, snake_case for methods).

### 2. The Constructor Mechanic
**Concepts**: `__init__`, Initialization  
**Task**: Implement a constructor for a `PatientRecord` that properly initializes five different attributes provided as arguments.

### 3. Mastering 'self'
**Concepts**: Object Scope, `self`  
**Task**: Fix a broken method that is trying to access instance variables without using `self`.

### 4. Instance Independence
**Concepts**: Instantiation  
**Task**: Instantiate three different `MedicalDevice` objects with unique serial numbers and demonstrate that they do not share state.

## Success Criteria
- All 4 syntax tests pass the internal runner.
- Class names are in PascalCase.
- Method names are in snake_case.
- All instance variables are accessed via `self`.
- No runtime errors during instantiation.
